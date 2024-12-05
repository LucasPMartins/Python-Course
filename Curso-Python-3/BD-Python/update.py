import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET weight = 80 '
    'WHERE id = 3'
)

cursor.close()
connection.close()