rows = int(input("Entter the number of rows: "))
n = rows
while n>=1:
	x = "*" * n
	y = " " * (rows - n)
	print(y + x)
	n -= 1
