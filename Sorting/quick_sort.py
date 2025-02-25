import numpy as np 
import time

def partition(arr,low,high): # đưa pivot về đúng vị trí là số nằm ở giữa dãy 
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    return arr  

for i in range(10):
    test_sq=np.loadtxt(f"dataset/seq_{i}.txt")
    start_time=time.time()
    print(quick_sort(test_sq,0,len(test_sq)-1))
    print("---%s seconds---" % (time.time()-start_time))


