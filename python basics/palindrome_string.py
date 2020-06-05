#s = input("Enter a string: ")
#z = s[::-1]
#if s==z:
#	print("The string is palindrome")
#else:
#	print("The string is not a palindrome")



#using function
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print("Oh no, not a palindrome")
