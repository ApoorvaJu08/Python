# program to remove white spaces from a string
def remove_white(string):
    l = []
    for i in range(len(string)):
        if string[i] != " ":
            l.append(string[i])
    return "".join(l)

a = input()
print(remove_white(a))