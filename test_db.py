import sqlite3
import json


def load_data_to_database(database_name, data_dict):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Создание таблицы, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()

    # Запись данных из словаря в таблицу
    for key, value in data_dict.items():
        cursor.execute('''INSERT OR REPLACE INTO my_table (key, value) VALUES (?, ?)''', (key, json.dumps(value)))

    conn.commit()
    conn.close()


load_data_to_database('my_database.bd', {"212": {"ARS_MOR": [1, 2, 3, 4, 5, 6, 10, 10, 10]}})
