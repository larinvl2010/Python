N = int(input("Введите количество дней N:"))
k = 0
maximum = 0
for i in range(0 , N):
    temp = int(input("Введите значение температуры: "))
    if temp >= 0:
        k +=1
        if maximum < k:
            maximum = k
    else:
        k = 0
print(f"Максимальная оттепель составила {maximum} дней")