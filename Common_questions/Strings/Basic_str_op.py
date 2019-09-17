# Program to perform basic string operations

# printing the string
a = input()
c = input()
print("The string is: ", a)

# printing the length of the string
print("Length of the string is: ", len(a))

# program to copy a string
b = a
print("String1 = ", a, "\nString2 = ", b)

# reverse a string
print("The reversed string is: ", a[::-1])

#concatenate 2 strings
print("Concatenated string is: ", a+c)

#compare
if(a == c):
    print("Strings are equal")
else:
    print("Strings are not equal")