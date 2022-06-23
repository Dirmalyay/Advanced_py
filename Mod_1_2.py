# Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в
# последовательности только чётные числа.

def even_funk(fn):
    def new_f(*args):
        f = fn(*args)
        b = filter(lambda x: x % 2 == 0, f)
        return b
    return new_f


@even_funk
def fib(n):
    first, second = 0, 1
    for i in range(n+1):
        first, second = second, first + second
        yield second


print(list(fib(10)))
