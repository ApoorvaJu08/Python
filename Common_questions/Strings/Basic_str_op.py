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

# program to find length of string without using len function
count = 0
for i in a:
    count += 1
print("length of string is: ", count)

# program to toggle each character in a string without using swapcase
str1 = ""
for i in range(len(a)):
    if a[i] >= "a" and a[i] <= "z":
        str1 = str1 + chr((ord(a[i])-32))
    elif a[i] >= "A" and a[i] <= "Z":
        str1 = str1 + chr((ord(a[i]) + 32))
    else:
        str1 = str1 + a[i]
print("String after the characters are toggled: ", str1)