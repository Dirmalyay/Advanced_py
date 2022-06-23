# Замените назначение на MCC и используйте его для определения назначения платежа
import sqlite3


try:
    sq_connect=sqlite3.connect('money_list.db')
    cursor = sq_connect.cursor()
    sq_rename_column = """alter table money_list_1 rename use to mcc"""
    cursor.execute(sq_rename_column)
    sq_fillin_column = """update money_list_1 set mcc = 4466"""
    cursor.execute(sq_fillin_column)
    sq_connect.commit()

    records = cursor.fetchmany(100)
    print(records)
    cursor.close()
except sqlite3.Error as error:
    print("Connection error", error)
finally:
    if sq_connect:
        sq_connect.close()
        print("Connection closed")
