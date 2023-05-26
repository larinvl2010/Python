print ("Введите номер билета")
number = int(input())
sum1=0
sum2=0
firstpart= number//1000
while firstpart>0 :
        x=firstpart%10
        sum1=sum1+x
        firstpart=firstpart//10
secondpart= number%1000
while secondpart>0 :
        y=secondpart%10
        sum2=sum2+y
        secondpart=secondpart//10
if sum1 == sum2:
    print ("Билет счастливый!")
else: print ("Билет не счастливый")