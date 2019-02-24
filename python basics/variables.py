"""First we are assigning 9 to a, then calling change function, inside of that we are assigning 90 to a and printing a. After the function call we are again printing the value of a. When we are writing a = 90 inside the function, it is actually creating a new variable called a, which is only available inside the function and will be destroyed after the function finished. So though the name is same for the variable a but they are different in and out side of the function."""

def change(b):
	a = 90
	print(a)
a = 9
print("Before the function call",a)
print("inside change function", end=' ')
change(a)
print("After the function call",a)


"""Here by using global keyword we are telling that a is globally defined, so when we are changing a’s value inside the function it is actually changing for the a outside of the function also."""

def change1(b):
	global a
	a = 90
	print(a)
a = 9
print("Before the function call",a)
print("inside change function", end=' ')
change1(a)
print("After the function call",a)



