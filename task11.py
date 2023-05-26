input_num = int(input('Введите число: '))

n1, n2 = 0, 1   # 0 1 1 2 3 5 8
f_id = 2
while n2 < input_num:
    n1, n2 = n2, n1 + n2
    f_id += 1
if input_num != n2:
    f_id = -1
print(f_id)