print ("Введите число")
number = int(input())
sum = 0
if number > 99 and number < 1000:
    while number>0 :
        x=number%10
        sum=sum+x
        number=number//10
    print (f"Cумма числа={sum}")
else: print ("Число не трёхзначное")