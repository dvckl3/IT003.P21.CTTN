import os
import numpy as np

data_path = "/home/duc112006/DSA/sorting" 
output_file = "/home/duc112006/DSA/sorting/all_testcases.txt" 

test_files = sorted([f for f in os.listdir(data_path) if f.endswith(".npy")])

with open(output_file, "w") as out_f:
    for file in test_files:
        file_path = os.path.join(data_path, file)
        data = np.load(file_path)

        out_f.write(f"{file}\n") 
        out_f.write(" ".join(map(str, data)) + "\n") 
        out_f.write("\n")  

print(f"Tất cả test cases đã được lưu vào {output_file}")

# file all_testcases.txt quá nặng nên e ko push lên được, file py này để convert npy sang txt
# lý do phải convert vì cpp k đọc trực tiếp data từ npy được

