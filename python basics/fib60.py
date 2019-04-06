n1, n2 = 0, 1
n3 = 0
li = []
for i in range(3, 61):
    n3 = n1 + n2
    li.append(n3)
    n1 = n2
    n2 = n3
print(li[-1])