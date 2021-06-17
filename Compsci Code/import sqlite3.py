import sqlite3
import uuid

database_filename = "tasker.db"

def database_write(sql, data = None):
    connection = sqlite3.connect(database_filename)
    connection.row_factory = sqlite3.Row
    db = connection.cursor()
    if data:
        rows_affected = db.execute(sql,data).rowcount
    else:
        rows_affected = db.execute(sql).rowcount
    connection.commit()
    db.close()
    connection.close()
    return rows_affected