# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# sp = [1, 2, 3, 4, 5]
# print(sp[3:]), print(sp[:3])
# print(sp[3:])
# print(sp[:3])
# print(sp[-2:])
# print(sp)

list_1 = [1, 2, 3, 4, 5]
k = 3
list_2 = list_1[k:] + list_1[0:k]
print(list_2)