# Создать функцию, которая принимает список из элементов типа int, а возвращает новый список из строковых
# значений исходного массива. Добавить аннотацию типов для входных и результирующих значений функции.
from typing import List


arg_list_1: List[int] = [
    1, 5, 6, 102, 15, 77, 'b', 10, 5, 89, (12, 66)
]


def convert(arg_list: List[int]) -> List[str]:

    ''' This function converts list of integer values to list strings values.'''
    res = []
    for i in arg_list:
        try:
            if int(i):
                i = str(i)
        except TypeError:
            continue
        except ValueError:
            continue
        res.append(i)
    return res


print(convert(arg_list_1))
