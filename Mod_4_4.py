# Измените таблиц так, чтобы можно было добавить не только расходы, а и доходы
import sqlite3


try:
    sq_connect = sqlite3.connect('money_list.db')
    cursor = sq_connect.cursor()
    sq_add_column_querty = """alter table money_list_1 add column income"""
    cursor.execute(sq_add_column_querty)
    sq_connect.commit()
    print("Column added")
    cursor.close()
except sqlite3.Error as error:
    print("Connection error", error)
finally:
    if sq_connect:
        sq_connect.close()
        print("Connection closed")
