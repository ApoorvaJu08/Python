#ask user for name
name = input("what is your name?: ")
#ask user for age
age = input("what is your age?: ")
#ask user for city
city = input("which city do you live in?: ")
#ask user what they enjoy
love = input("what do you love doing?: ")
#create output text
string = "Your name is {} and you are {} years old. You live in {} city and you love {}."
output = string.format(name,age,city,love)
#print output to screen
print(output)
