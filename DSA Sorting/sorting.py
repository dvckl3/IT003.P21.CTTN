# tất cả các thuật sort
import numpy as np 
import time
import os

def numpy_sort(arr):
    return np.sort(arr)


 
def median_of_three(arr, l, h):
    mid = (l + h) // 2
    a, b, c = arr[l], arr[mid], arr[h]
    if a > b: a, b = b, a
    if a > c: a, c = c, a
    if b > c: b, c = c, b
    if b == arr[l]: return l
    elif b == arr[mid]: return mid
    else: return h

def partition(arr, l, h):
    pivot_idx = median_of_three(arr, l, h)
    arr[pivot_idx], arr[h] = arr[h], arr[pivot_idx]
    pivot = arr[h]
    i = l - 1  
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[h] = arr[h], arr[i + 1]  
    return i + 1

def quick_sort(arr):
    l, h = 0, len(arr) - 1
    if l >= h:
        return arr  
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        p = partition(arr, l, h)
        if p - 1 > l:
            stack.append((l, p - 1))
        if p + 1 < h:
            stack.append((p + 1, h))
    return arr  



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1
    return arr

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr  



