def findSum(str1): 
  
    temp = "" 
  
    Sum = 0
  
    for ch in str1: 
  
        # if current character is a digit 
        if (ch.isdigit()): 
            temp += ch 
  
        # if current character is an alphabet 
        else: 
              
            # increment Sum by number found  
            # earlier(if any) 
            Sum += int(temp) 
  
            # reset temporary str1ing to empty 
            temp = "0"
          
    return Sum + int(temp) 
  
str2 = input()
print(findSum(str2)) 