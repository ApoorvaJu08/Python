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
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(frequ(str1)))