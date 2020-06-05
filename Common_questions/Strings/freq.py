# program to count frequency of each letter in a string
def frequ(test_str):
    all_freq = {} 
    
    for i in test_str: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    return all_freq

str1 = input()  
str2 = input()
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(frequ(str1)))

#to check if 2 strings are anagram or not
res1 = frequ(str1)
res2 = frequ(str2)
if res1 == res2:
    print("anagram")
else:
    print("not anagram")

#or
if(sorted(str1) == sorted(str2)):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")