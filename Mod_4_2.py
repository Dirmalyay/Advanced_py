# Создать консольный интерфейс (CLI) на Python для добавления новых записей в базу данных
import sqlite3


def insert_data_row(use, amount, date):
    try:
        sq_connect = sqlite3.connect('money_list.db')
        cursor = sq_connect.cursor()
        print("Data base connected")
        sqlite_insert_query = """INSERT or IGNORE INTO money_list_1
                    (use,amount,date) VALUES(?, ?, ?)"""
        data = (use, amount, date)
        cursor.execute(sqlite_insert_query, data)
        sq_connect.commit()
        print("Data inserted successful", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Connection error", error)
    finally:
        if sq_connect:
            sq_connect.close()
            print("Connection closed")
while True:
    print("My expenses. Add more data:")
    try:
        u = input("Enter spending area: ")
        a = int(input("Enter amount: "))
        d = input("Enter the date(dd.mm): ")
        insert_data_row(u, a, d)
        q = input("Press + if you want add one more data. For exit press q. ")
        if q != '+' or q == 'q':
            break
    except ValueError:
        print("Invalid value.")

