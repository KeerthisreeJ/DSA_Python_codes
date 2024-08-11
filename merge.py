from numpy import Infinity, inf


def MergeSort(A,start,end):
    if start<end:
        mid = (start+end)//2
        MergeSort(A,start,mid)
        MergeSort(A,mid+1,end)
        Merge(A,start,mid,end)
    
    else :
        return 1


def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
   
    L = [0]*(n1+2)
    
    R = [0]*(n2+2)
    for i in range (1, n1+1):
        L[i] = A[p+i-1]
    
    for j in range(1,n2+1):
        R[j] = A[q+j]

    L[n1+1] = 999
    R[n2+1]  = 999
    print("L: ",L , "   R: ",R)
    

    i = 1
    j = 1

    for k in range (p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i=i+1
        else :
            A[k] = R[j]
            j = j+1

A = [34,65,32,7,2,0,24,65,0]
MergeSort(A,0,8)
print(A)

