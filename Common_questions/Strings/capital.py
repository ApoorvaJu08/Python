# program to capitalize first and last letter of each word in a line
def capitalize_first_last_letter(str1):
    str1 = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]

string = input()
print(capitalize_first_last_letter(string))