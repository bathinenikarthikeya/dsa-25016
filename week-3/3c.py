def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1
    while i<len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1
    while j<len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1
    return arr
arr=[]
n=int(input("enter the no of elements in list:"))
for k in range(n):
      nums=int(input(f"enter the {k+1}th number:"))
      arr.append(nums)
merge_sort(arr)
print(arr)
