flag=0
array=[2,3,4,5,10,59,89,78,900]
target=int(input("enter item"))
for counter in array:
    if flag==1:
        print("item is found")
        break
if flag==0:
    print("item is not found")    
