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
z= []
combo= []
count =0
for i in range(0,n,1):
   for j in range(i,n,1):
      if x[i] not in m:
         if x[i] == x[j]:
            count = count+1
      else:
         break
   if x[i] not in z:
   	z.append(x[i])
   	m.append(count)
   count=0

def SS(z,m):
  for start in range(len(m)): 
    minpos = start
    for i in range(start,len(m)):
       if m[i] < m[minpos]:
           minpos = i
    (m[start],m[minpos]) = (m[minpos],m[start])
    (z[start],z[minpos]) = (z[minpos],z[start])

SS(z,m)

for p in range(0,len(z),1):
      combo.append((z[p],m[p]))



# >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#for x in [1,2,3]:
#...     for y in [3,1,4]:
#...         if x != y:
#...             combs.append((x, y))

