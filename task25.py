# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

sp = input().split()
sl = {}
res = ''
for i in sp:
    if i not in sl:
        res += f"{i} "
    else:
        res += f"{i}_{sl[i]} "
    sl[i] = sl.get(i, 0) + 1
print(res.strip())

---

sp = input().split()
sl = {}
res = ''
for i in sp:
    if i not in sl:
        res += i + ' '
        sl[i] = 1
    else:
        res += i + '_' + str(sl[i]) + ' '
        sl[i] += 1
print(res)

---

s = "a a a b c a a d c d d"
lst = s.split()
d = {}
for i in range(len(lst)):	
	d[lst[i]] = d.get(lst[i], -1) + 1
	if d[lst[i]] > 0:
		lst[i] += '_' + str(d[lst[i]]) 
	
print(*lst)