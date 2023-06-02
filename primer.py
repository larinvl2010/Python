# a = list()
# b = []
# b.append(10)
# n = 5
# m = 10
# for i in range(n, m):
#     a.append(i)
# print(a)
# print(b)
# sp = [4, 5, 2, 8]
# for i in range(len(sp)):
#     if i == 3:
#         sp[i] = 100
#     print(sp[i])
# for i in sp:
#     print(i)

# sp = [1, 2, 3, 4, 5, 6]
# print(sp[:3])
# print(sp[3:])
# print(sp[-2:])
# sp = sp[::-1]
# print(sp)

# mn = set()
# mn = {1, 2, 3}
# mn.add(4)
# mn.add(4)
# print(mn)
# sp = [1, 1, 2, 2, 3, 3]
# print(*set(sp))

# sl = dict()
# sl = {"login": "vasya", "password": "123"}
# print(sl["login"])
# sl["address"] = "Moscow"
# print(sl)
# print(list(sl.keys()))
# print(list(sl.values()))
# for key, value in sl.items():
#     print(key, '-', value)
# print(list(sl.items()))
# sl = dict(sorted(list(sl.items())))
# print(sl)
# http://ya.ru?search=собака
#
# {"search": "собака"}

# coords = 1, 2
# coords1 = sorted(coords)
# print(coords[0], coords[1])
#
#
# def get_coords():
#     x = 4
#     y = 5
#     return x, y

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # for i in matrix:
# #     print(*i)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i % 2 == 0 and j % 2 != 0:
#             matrix[i][j] += 10
#         print(matrix[i][j], end=' ')
#     print()

# sp = [1, 2, 3]
# sp2 = sp.copy()
# sp3 = sp[:]
# sp.append(5)
# print(sp)
# print(sp2)

sp = [1, 2, 3]
print(dir(sp))
help(sp.insert)
sp.insert(0, 8)
print(sp)