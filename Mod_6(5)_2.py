# Создайте три функции, одна из которых читает файл на диске с заданным именем и проверяет наличие строку “Wow! ”.
# В случае, если файла нет, то засыпает на 5 секунд, а затем снова продолжает поиск по файлу. В случае, если файл есть,
# то открывает его и ищет строку “Wow!”. При наличии данной строки закрывает файл и генерирует событие, а другая
# функция ожидает  данное событие и в случае его возникновения выполняет удаление этого файла. В случае если
# строки «Wow!» не было найдено в файле, то засыпать на 5 секунд. Создайте файл руками и проверьте выполнение программы.
import asyncio
import os
import time
from asyncio.coroutines import iscoroutine


def open_file2():
    if (os.path.isfile("data1.txt")):
        file = (open("data1.txt", 'r'))
        var = looking_for_string(file)
        return var
    else:
        asyncio.sleep(10)
        try:
            file = (open("data1.txt", 'r'))
            var = looking_for_string(file)
            return var
        except FileNotFoundError:
            print("File not found.")


def looking_for_string(file):
    result = False
    for i in file:
        if i == "Wow!\n":
            print("Your string exist in file.")
            result = True
            file.close()
            break
    else:
        print("No string.")
    return result


def delete_file():
    var = yield
    if var:
        os.remove("data1.txt")
        print("File deleted.")
    else:
        asyncio.sleep(5)
        print("Waiting 5 sec.")


'''
Не работает тут это
open_file2()
event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(delete_file())
]

tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()'''

print(iscoroutine(delete_file()))

f = open_file2()
cor = delete_file()
cor.send(None)
# StopIteration I don't know why.
cor.send(f)
cor.close()
