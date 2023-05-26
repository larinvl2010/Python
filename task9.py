print ("Введите число")
number = int(input())
i=1
sum=1
while i<=number:
    sum=sum*i
    i=i+1
print (f"Факториал числа {number}={sum}")