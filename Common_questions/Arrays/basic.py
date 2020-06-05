# insert an element in an array
# n = int(input())
arr = [1, 2, 3, 4, 5]
pos = int(input())
ele = int(input())
arr.insert(pos, ele)
for i in range(0, len(arr)):
    print(arr[i])

#delete an element
arr.remove(arr[pos])

#search an element
item_to_be_searched = int(input())
for i in range(len(arr)):
    if arr[i] == item_to_be_searched:
        print("Element found at index ", i)
# else:
#     print("Element not found in the array")