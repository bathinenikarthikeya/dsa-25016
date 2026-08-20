def quick_sort(a,low,high):
    if low<high:
        i=low
        j=high
        pivot=low
    while i<j:
        while i<lan(a) and a[i]<=a[pivot]:
            i=i+1
        while a[j]>a[pivot]:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[j],a[pivot]=a[pivot],a[j]
    return a
a=list(map(int,input("enter number to sort:").split("")))
n=len(a)
quicksort(a,0,n-1)
print(a)
