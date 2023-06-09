def in_out(n):
	if n == 0:
		return
	k = input('Введите число: ' )
	in_out(n - 1)
	print(k, end=' ')



n = int(input('Введите число N: '))
in_out(n)