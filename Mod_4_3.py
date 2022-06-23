# Создать агрегатные функции для подсчёта общего количества расходов и расходов за месяц.
# Обеспечить соответствующий интерфейс для пользователя.
import sqlite3


def spend_in_month(date1):
    try:
        sq_connect = sqlite3.connect('money_list.db',
                                     detect_types=sqlite3.PARSE_DECLTYPES |
                                     sqlite3.PARSE_COLNAMES)
        cursor = sq_connect.cursor()
        print("Data base connected")
        sq_select_querty = """SELECT * from money_list_1 where date == ?"""
        cursor.execute(sq_select_querty, (date1,))
        records = cursor.fetchmany(100)
        print(date1)
        # print("all rows", len(recors))
        date_serch = date1.split('.')
        amount_1 = 0
        for row in records:
            print('use', row[1])
            date_in_base = row[3]
            d = date_in_base.split('.')
            if d[1] == date_serch[1]:
                amount_1 += row[2]
        print(amount_1)

        cursor.close()
    except sqlite3.Error as error:
        print('Connecting error', error)
    finally:
        if sq_connect:
            sq_connect.close()
            print('Connection closed')


spend_in_month('19.06')
