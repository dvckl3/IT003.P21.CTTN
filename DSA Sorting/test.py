from sorting import *
import time
import os
import json

data_path = "/home/duc112006/DSA/sorting/all_testcases.txt"
result_path = "/home/duc112006/DSA/sorting/result/time.json"

result = {}

algorithm = {
    "numpy_sort": numpy_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "heap_sort": heap_sort
}

with open(data_path, "r") as f:
    lines = f.readlines()
test_cases = {}
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    
    test_case_name = line
    i += 1
    if i >= len(lines): 
        break  

    try:
        data = list(map(float, lines[i].strip().split()))  
        test_cases[test_case_name] = data 
        print(test_cases)
    except ValueError:
        i += 1
        continue

    result[test_case_name] = {}

    for name, func in algorithm.items():
        arr = data.copy()
        start_time = time.time()
        func(arr)
        end_time = time.time()
        run_time = (end_time - start_time) * 1000  
        result[test_case_name][name] = round(run_time, 6)
        print(f"{test_case_name} {name} {run_time:.6f}ms")

    i += 1  

os.makedirs(os.path.dirname(result_path), exist_ok=True)
with open(result_path, "w") as f:
    json.dump(result, f, indent=4)
