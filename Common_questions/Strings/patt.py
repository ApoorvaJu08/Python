# program to find frequency of pattern 0(1+)0 in the string
def find_pattern(str):
    last = str[0]
    i = 1
    counter = 0
    while(i < len(str)):
        if(str[i] == '1' and last == '0'):
            while str[i] == '1':
                i += 1
            if str[i] == '0':
                counter += 1
        last = str[i]
        i += 1
    return counter

str1 = input("Enter the string : ")
ans = find_pattern(str1)
print("Number of patterns : ",ans)