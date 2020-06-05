m= int(input("Enter first number"))
n= int(input("Enter second number"))

def divides(m,n):
	if n%m == 0:
		return(True)
	else:
		return(False)

def even(n):
	return(divides(2,n))

def odd(n):
	return(not divides(2,n))


#factors of a number

def fact(n):
	factl = []
	for i in range(i,n+1):
		if n%i == 0:
			factl = factl + [i]
	return(factl)

#power

def power(x,n):
	ans = 1
	for i in range(0,n):
		ans = ans * x
	return(ans)
