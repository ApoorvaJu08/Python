#n = int(input("Enter the number"))
def pattern(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print("* ",end="")
		print("\r")


def pattern1(a):
	k = 2*a - 2
	for p in range(0,a):
		for q in range(0,k):
			print(end=" ")
		k = k - 2
		for q in range(0,p+1):
			print("* ", end="")
		print("\r")

def triangle(a):
	k = 2*a - 2
	for p in range(0,a):
		for q in range(0,k):
			print(end=" ")
		k = k - 1
		for q in range(0,p+1):
			print("* ", end="")
		print("\r")

