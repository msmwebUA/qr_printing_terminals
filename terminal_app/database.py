# Class for database operations

import sqlite3 as db
from contextlib import closing
from datetime import datetime
from random import randint

class Database:
  def __init__(self, config: object) -> None:
    self.config = config
    # create tables if not exist
    self.execute({
      "query": f"""
        CREATE TABLE IF NOT EXISTS {self.config.db_log_table} (
          "id" INTEGER PRIMARY KEY, 
          "emp_id" INTEGER NOT NULL, 
          "copies" INTEGER NOT NULL, 
          "timestamp" DATETIME DEFAULT CURRENT_TIMESTAMP,
          "error_msg" TEXT
        )""",
      "many": False,
      "data": ()
    })
    self.execute({
      "query": f"""
        CREATE TABLE IF NOT EXISTS {self.config.db_label_id_table} (
          "label_id" INTEGER NOT NULL
        )""",
      "many": False,
      "data": ()
    })
    # create indexes if not exist
    self.execute({
      "query": f'CREATE INDEX IF NOT EXISTS {self.config.db_label_id_table}_index ON {self.config.db_label_id_table} ("label_id")',
      "many": False,
      "data": ()
    })

  def addLogEntry(self, emp_id: str, copies: str, error_msg: str) -> None:
    """
    Adds a log entry to the database.
    
    Parameters:
    emp_id (int): employee id
    copies (int): number of copies printed
    error_msg (str): error message if any
    """
    self.execute({
      "query": f'INSERT INTO {self.config.db_log_table} ("emp_id", "copies", "error_msg") VALUES (?, ?, ?)',
      "many": False,
      "data": (emp_id, copies, error_msg) # emp_id will be converted to int inside db
    })

  def addLabelId(self, label_ids: list[(int)]) -> None:
    """
    Adds label IDs to the database.
    
    Parameters:
    label_ids (list[int]): list of tuples of label IDs
    """
    self.execute({
      "query": f'INSERT INTO {self.config.db_label_id_table} VALUES (?)',
      "many": True,
      "data": label_ids
    })
  
  def execute(self, params: dict) -> None:
    
    """
    Executes a database query with parameters.

    Parameters:
    params (dict): dictionary with query, many and data keys.
    "query" (str): SQL query to execute
    "many" (bool): True if query is meant to be executed with executemany
    "data" (list of tuples or tuple): parameters to pass to the query
    
    Raises:
    db.Error: if a database error occurs
    """
    try:
      with closing(db.connect(self.config.db_file)) as connection:
        with connection:
          cursor = connection.cursor()
          if params["many"]:
            cursor.executemany(params["query"], params["data"])
          else:
            cursor.execute(params["query"], params["data"])
    except db.Error as e:
      self.addDbLogEntry(e)

  def generateLabelData(self, data: dict) -> dict:
    """
    Generates data for labels. Returns dict with emp_id as str in XXXX format and label_ids as list.
    
    Parameters:
    data (dict): dictionary with data passed from label object
    
    Returns:
    dict: dictionary with emp_id and label_ids, or None if no free label IDs were found
    """
    try:
      with closing(db.connect(self.config.db_file)) as connection:
        with connection:
          cursor = connection.cursor()
          for i in range(data["copies"]):
            exists = True
            while exists:
              label_id = randint(self.config.label_id_min, self.config.label_id_max)
              db_label_id = int(f"{data['emp_id']}{label_id}")
              # Check if label_id already exists in database
              cursor.execute(f"SELECT 1 FROM {self.config.db_label_id_table} WHERE label_id = ?", (db_label_id,))
              if not cursor.fetchone():
                exists = False
                data["label_ids"].append(str(label_id))
      if data["label_ids"]:
        return data
      else:
        return None
    except db.Error as e:
      self.addDbLogEntry(e)

  def getCopiesLeft(self, emp_id: str) -> int:
    """
    Returns number of copies left for employee (for current day).
    
    Parameters:
    emp_id (str): employee id
    
    Returns:
    int: number of copies left
    """
    day_limit = self.config.printer_max_copies_day
    with closing(db.connect(self.config.db_file)) as connection:
      with connection:
        cursor = connection.cursor()
        printed_copies = cursor.execute(f"SELECT COALESCE(SUM(copies), 0) FROM {self.config.db_log_table} WHERE emp_id = ? AND timestamp > datetime('now', '-1 day') AND error_msg IS NULL", (emp_id,)).fetchone()[0]
    return day_limit - printed_copies

  def addDbLogEntry(self, e: str) -> None:
    """
    Adds database error to log file instead table.
    
    Parameters:
    e (str): error message
    """
    with open(self.config.db_error_log_file, "a") as f:
      f.write(f"{datetime.now():%d.%m.%Y %H:%M:%S} - {e}\n")
    print(f"Database error: {e}")
