# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


from functools import lru_cache


@lru_cache()
def fib_r(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib_r(n - 1) + fib_r(n - 2)


print(fib_r(100))