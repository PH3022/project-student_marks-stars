import sqlite3
import json


def read_data_from_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Создание таблицы, если она еще не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()

    # Чтение данных из таблицы
    cursor.execute('''SELECT * FROM my_table''')
    rows = cursor.fetchall()

    data_dict = {}
    for row in rows:
        key = row[0]
        value = json.loads(row[1])
        data_dict[key] = value

    conn.close()
    return data_dict


database_dict = read_data_from_database('project_student_marks_database.bd')
print(database_dict)