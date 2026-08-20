def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range (i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index], arr[i]
    return arr
arr=[]
n=int(input("enter the no of elements in list:"))
for k in range(n):
      nums=int(input(f"enter the {k+1}th number:"))
      arr.append(nums)
selection_sort(arr)
print(arr)
