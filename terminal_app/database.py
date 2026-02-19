# Class for database operations

import sqlite3 as db
from datetime import datetime

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
      with db.connect(self.config.db_file) as connection:
        cursor = connection.cursor()
        if params["many"]:
          cursor.executemany(params["query"], params["data"])
        else:
          cursor.execute(params["query"], params["data"])
        connection.commit()
    except db.Error as e:
      # Add database error to log file instead table
      with open(self.config.db_error_log_file, "a") as f:
        f.write(f"{daterime.now().strftime('%d.%m.Y %H:%M:%S')} - {e}")
      print(f"Database error: {e}")