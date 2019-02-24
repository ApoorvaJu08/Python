#triplets
for x in range(101):
a = 0
	for y in range(x,101):
		a = x*x + y*y
		for z in range(101):
			if a == z*z:
print(x,y,z) 


#matrix 
[[0 for x in range(3)] for y in range(4)]
