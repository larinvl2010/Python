# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

sp=[1,3,4,3,1]

def min(x):
    mn=x[0]
    for i in x:
        if i < mn:
            mn = i
    return mn

def max(x):
    mx=x[0]
    for i in x:
        if i > mx:
            mx = i
    return mx
        
def change(max, min, x):
    for i in range(len(x)):
        if x[i] == max:
            x[i]=min
    return x
print (max(sp))
print(change(max(sp),min(sp),sp))