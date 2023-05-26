print ("Введите количество строк")
row = int(input())
print ("Введите количество столбцов")
column = int(input())
print ("Введите количество оторванных ячеек")
part = int(input())
if part%row==0 or part%column==0 and column*row<=part:
    print ("Оперция возможна")
else : 
    print ("Оперция невозможна")
