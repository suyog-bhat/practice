def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range (len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j̦
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range (i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr=i
        while curr>0:
            if arr[curr]<arr[curr-1]:
                temp=arr[curr]
                arr[curr]=arr[curr-1]
                arr[curr-1]=temp
            curr-=1
    return arr
def merge(larr,rarr):
    lptr=rptr=0
    res=[]
    while lptr<len(larr) and rptr<len(rarr):
        if larr[lptr]<rarr[rptr]:
            res.append(larr[lptr])
            lptr+=1
        else:
            res.append(rarr[rptr])
            rptr+=1
    if lptr<len(larr):
        res.extend(larr[lptr:])
    if rptr<len(rarr):
        res.extend(rarr[rptr:])
    return res
    
def mergesort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        l,r=mergesort(arr[:mid]),mergesort(arr[mid:])
        return merge(l,r)

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    for i in range(len(arr)):

print(bubble_sort([3,4,1,8,2,5]))
print(selection_sort([3,4,1,8,2,5]))
print(insertion_sort([3,4,1,8,2,5]))
print(mergesort([3,4,1,8,2,5]))
