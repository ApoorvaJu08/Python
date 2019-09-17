# program to remove all characters from a string except alphabets
import re
a = input()
result = re.sub(r'[^a-zA-Z]', "", a)
print(result)