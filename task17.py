# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
print ("Введите числа")
sp = [1,1,2,0,-1,3,4,4]
print(len(set(sp)))

sp = [1, 1, 2, 0, -1, 3, 4, 4]
sl = {}
for el in sp:
    sl[el] = sl.get(el, 0) + 1
    # if el not in sl:
    #     sl[el] = 1
    # else:
    #     sl[el] += 1
print(sl)
