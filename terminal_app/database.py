# Class for database operations

import sqlite3 as db
from contextlib import closing
from datetime import datetime
from random import randint

class Database:
  def __init__(self, config: object) -> None:
    self.config = config
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
    
    # TODO: create index for label_id table if not exists

  def addLogEntry(self, emp_id: str, copies: int, error_msg: str) -> None:
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
      # Add database error to log file instead table
      with open(self.config.db_error_log_file, "a") as f:
        f.write(f"{daterime.now().strftime('%d.%m.Y %H:%M:%S')} - {e}")
      print(f"Database error: {e}")

  @staticmethod
  def generateLabelData(config: object, data: dict) -> dict:
    """
    Generates data for labels. Returns dict with emp_id as str in XXXX format and label_ids as list.
    
    Parameters:
    config (object): application configuration
    data (dict): dictionary with data passed from label object
    
    Returns:
    dict: dictionary with emp_id and label_ids, or None if no free label IDs were found
    """
    with closing(db.connect(config.db_file)) as connection:
      with connection:
        cursor = connection.cursor()
        for i in range(data["copies"]):
          exists = True
          while exists:
            label_id = randint(config.label_id_min, config.label_id_max)
            db_label_id = int(f"{emp_id}{label_id}")
            print(db_label_id) # test purposes
            # Check if label_id already exists in database
            cursor.execute(f"SELECT 1 FROM {config.db_label_id_table} WHERE label_id = ?", (db_label_id,))
            if not cursor.fetchone():
              exists = False
              data["label_ids"].append(str(label_id))
    if data["label_ids"]:
      return data
    else:
      return None