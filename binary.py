def binary_search(array,target):
    array[1,2,3,4,5]
    target=4
    low,high=0,len(array)-1
    while low <=high:
        mid=min+(max-min)//2
        if array[mid]< target:
            min=mid-1
        else:
            max=mid-1
            return -1
 