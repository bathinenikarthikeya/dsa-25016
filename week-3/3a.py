def insertion_sort(arr):
    n=len(arr)
    for i in range (1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr=[]
n=int(input("enter the no of elements in list:"))
for k in range(n):
      nums=int(input(f"enter the {k+1}th number:"))
      arr.append(nums)
insertion_sort(arr)
print(arr)
