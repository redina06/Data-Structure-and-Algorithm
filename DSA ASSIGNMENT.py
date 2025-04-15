
#Write an alternative Python code for simple sorting algorithms, such as insertion and selection sorts.
#insertion sorting
arr = [29, 10, 14, 37, 13]
for i in range(1, len(arr)):
    key = arr[i]
    position=i
    for j in range(i-1,-1,-1):
        if arr[j] > key:
            arr[j+1] = arr[j]
            position=j
            break
    arr[position] = key

print(arr)

# as for the selection sortng
arr =[19,6,17,21,5]
n = len(arr)
for i in range(n - 1):
    j = i + 1
    min_index = i
    while j < n:
        while arr[j] < arr[min_index]:  
            min_index = j
        j += 1  
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)
            





