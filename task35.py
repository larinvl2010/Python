# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime(n):
	if n < 0:
		n = abs(n)
	if n == 0 or n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


n = int(input('Введите число: '))
print(('no','yes')[is_prime(n)])