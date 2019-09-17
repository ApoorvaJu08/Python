# program to remove brackets from an algebric expression
a = input()
brackets = ('()')
for i in a:
    if i in brackets:
        a = a.replace(i, "")
print(a)