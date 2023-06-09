a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)


print(f"Сумма числа {a} и {b} = {sum(a, b)}")