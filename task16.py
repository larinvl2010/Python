# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

print ("Введите размер списка")
x= int(input())
print ("Введите число, которое будем искать")
num = int(input())
print ("Введите числа списка")
list_1 = [] # создание пустого списка
for i in range(x-1): # цикл выполнится 5 раз
    n = int(input()) # пользователь вводит целое число
    list_1.append(n)
list_1.append(num)
print(list_1)
count=0
for i in range(x):
    if list_1[i]==num:
        count=count+1
print(f"Вышеуказанное число вводится {count} раз")

