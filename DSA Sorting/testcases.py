import numpy as np 
import os
import random as r


def generate_sequence(path):
    test_case=[]
    size=10**6
    test_case.append(np.arange(size))
    test_case.append(np.arange(size)[::-1])
    for i in range(8):
        test_case.append(np.random.uniform(-1e6,1e6,size))

    os.makedirs(path,exist_ok=True)

    for i,data in enumerate(test_case):
        file_path=os.path.join(path,f"testcase_{i}.npy")
        np.save(file_path,data)
        print(f"lưu file {file_path}")

save_dir="home/duc112006/DSA/sorting"

generate_sequence(save_dir)

if __name__ == "__main__":
    pass


