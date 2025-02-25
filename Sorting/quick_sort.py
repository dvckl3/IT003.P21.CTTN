import numpy as np
import time
import os

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def load_dataset(file_path):
    return np.loadtxt(file_path)

def main():
    dataset_dir = "/home/duc112006/DSA/dataset"
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(10):
        file_path = os.path.join(dataset_dir, f"seq_{i}.txt")
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        
        data = load_dataset(file_path)

        start_time = time.time()
        quicksort_iterative(data)
        elapsed_time = time.time() - start_time

        result_file = os.path.join(output_dir, f"sorted_sequence_{i}_quicksort.txt")
        np.savetxt(result_file, data, fmt="%.6f")

        print(f"Sorted sequence_{i}.txt in {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
