def quicksort(a, start, end):
    if start <end:
        ind = Partition(a,start,end)
        quicksort(a,start,ind-1)
        quicksort(a,ind,end)

def Partition(a,start,end):
    i = start
    j = end
    pivot = a[(start+end)//2]
    while(i<=j):
        while a[i] < pivot:
            i = i+1
        while a[j] >pivot:
            j = j-1
        if i <j:
            a[i],a[j]=a[j],a[i]
            print(a)
            i = i+1
            j = j-1
    return i 

a = [12,54,3,21,76,8,0,19,2]
print(quicksort(a,0,len(a)-1))
