import json
import matplotlib.pyplot as plt
import numpy as np

result_path = "/home/duc112006/DSA/sorting/result/time.json"

with open(result_path, "r") as f:
    data = json.load(f)

test_cases = list(data.keys())
algorithms = [algo for algo in (next(iter(data.values())).keys()) if algo !="numpy_sort"]
time_values = {algo: [data[case][algo] for case in test_cases] for algo in algorithms}
x = np.arange(len(test_cases))
width = 0.15

fig, ax = plt.subplots(figsize=(10, 6))

for i, algo in enumerate(algorithms):
    times = [data[tc][algo] for tc in test_cases]
    ax.bar(x + i * width, times, width, label=algo)

ax.set_xlabel("Test Cases")
ax.set_ylabel("ms (miliseconds)")
ax.set_title("So sánh các thuật sắp xếp chạy bằng Python")
ax.set_xticks(x + width * (len(algorithms) / 2))
ax.set_xticklabels(test_cases, rotation=45, ha="right")
ax.legend()
plt.tight_layout()
plt.show()
