number = -1
input_number = -1
max_number = -1
while input_number != 0:
    input_number = int(input())    
    max_number = input_number if input_number > max_number else max_number
print(max_number)