# Сделать таблицу для подсчёта личных расходов со следующими полями: id, назначение, сумма, время.
import sqlite3


try:
    sq_connect = sqlite3.connect('money_list.db')
    sq_create_table = '''CREATE TABLE IF NOT EXISTS money_list_1 (id INTEGER PRIMARY KEY, 
                    use TEXT NOT NULL,
                    amount INTEGER NOT NULL,
                    date TEXT NOT NULL);'''
    cursor = sq_connect.cursor()
    print("Data base connected")
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("DB version: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Connection error", error)
finally:
    if sq_connect:
        sq_connect.close()
        print("Connection closed")
