"""Создайте функцию по вычислению факториала числа. Запустите несколько задач, используя ThreadPoolExecutor и замерьте
скорость их выполнения, а затем замерьте скорость вычисления, используя тот же самый набор задач на ProcessPoolExecutor.
В качестве примеров, используйте крайние значения, начиная от минимальных и заканчивая максимально возможными, чтобы
увидеть прирост или потерю производительности.
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def factorial(started=1, finish=1):
    result = started
    for i in range(started, finish):
        result *= i
    return result


def run_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future1 = executor.submit(factorial, started=1, finish=2 ** 3)
    future2 = executor.submit(factorial, started=2 ** 3, finish=2 ** 5)

    result = future2.result() + future1.result()
    print('Result: {result}. Time for {executor}: {spent_time}'.format(result=result, executor=executor_class.__name__,
                                                                       spent_time=time.time() - started))


def run_by_executor_map(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    params = [
        [0, 2 ** 3],
        [2 ** 3, 2 ** 5]
    ]
    result = sum(executor.map(factorial, *params))
    print('Result: {result}. Time for {executor}: {spent_time}'.format(result=result, executor=executor_class.__name__,
                                                                       spent_time=time.time() - started))


if __name__ == '__main__':
    print('Execute using map...')
    run_by_executor_map(ThreadPoolExecutor)
    run_by_executor_map(ProcessPoolExecutor)

    print('Execute using submit...')
    run_executor(ThreadPoolExecutor)
    run_executor(ProcessPoolExecutor)
