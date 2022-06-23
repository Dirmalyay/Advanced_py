# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.

# list_whole_num = [x**2 for x in range(20) if x % 2 != 0]
# print(list_whole_num)

import random

whole_num = [random.randint(0, 200) for i in range(100)]
odd_num = list(filter(lambda x: x % 2 != 0, whole_num))
print(odd_num)
odd_num_sqr = list(map(lambda y: y**2, odd_num))
print(odd_num_sqr)
