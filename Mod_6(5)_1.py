# Создайте функцию по вычислению факториала числа. Запустите несколько задач, используя ThreadPoolExecutor и
# замерьте скорость их выполнения, а затем замерьте скорость вычисления, используя тот же самый набор задач на
# ProcessPoolExecutor. В качестве примеров, используйте крайние значения, начиная от минимальных и заканчивая
# максимально возможными, чтобы увидеть прирост или потерю производительности.
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


n = int(input("Enter the number to calculate factorials: "))


def run_by_executer(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started_at = time.time()
    result = executor.map(factorial(n))
    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started_at))


run_by_executer(ThreadPoolExecutor)
run_by_executer(ProcessPoolExecutor)
