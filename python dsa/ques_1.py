x = input('Enter your list: ')
x = [int(y) for y in x.split(',')]

def SelectionSort(x):
# Scan slices x[0:len(x)], x[1:len(x)], ...
  for start in range(len(x)): 
    # Find minimum value in slice . . .
    minpos = start
    for i in range(start,len(x)):
       if x[i] < x[minpos]:
           minpos = i
    # . . . and move it to start of slice
    (x[start],x[minpos]) = (x[minpos],x[start])

SelectionSort(x)
n = len(x)
m = []
count =0
for i in range(0,n,1):
   for j in range(i,n,1):
      if x[i] not in m:
         if x[i] == x[j]:
            count = count+1
      else:
         break
   if x[i] not in m:
   	m.append(x[i])
   	m.append(count)
   count=0
for z in range(0,n,2):
	print(m[z],m[z+1])
