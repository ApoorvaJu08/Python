# program to sort a string in alphabetical order
a = input()
tmp = 0
str = list(a)
for i in range(0, len(str)):
    for j in range(0, len(str)):
        if str[j] > str[i]:
            tmp = str[i]
            str[i] = str[j]
            str[j] = tmp
print("".join(str))

#using standard functions
print("".join(sorted(str)))