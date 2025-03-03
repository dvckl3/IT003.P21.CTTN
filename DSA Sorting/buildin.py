import json
import matplotlib.pyplot as plt


json_path = "/home/duc112006/DSA/sorting/result/time.json"
cpp_result_path = "/home/duc112006/DSA/sorting/cpp_sort.txt"


with open(json_path, "r") as f:
    json_data = json.load(f)


cpp_results = {}
with open(cpp_result_path, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) == 2:
            testcase, time_ms = parts
            testcase = testcase.strip()
            time_ms = float(time_ms.replace("ms", ""))
            cpp_results[testcase] = time_ms


common_testcases = sorted(set(json_data.keys()) & set(cpp_results.keys()))


numpy_times = [json_data[tc]["numpy_sort"] for tc in common_testcases]
cpp_times = [cpp_results[tc] for tc in common_testcases]


plt.figure(figsize=(10, 5))
plt.plot(common_testcases, numpy_times, marker="o", markersize=6, label="numpy.sort() (ms)", linestyle="--")
plt.plot(common_testcases, cpp_times, marker="s", markersize=6, label="std::sort (ms)", linestyle="-")


plt.xlabel("Test Cases")
plt.ylabel("Time (ms)")
plt.title("Comparison of numpy.sort() vs C++ std::sort")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(y=0, color="black", linewidth=0.8)


plt.tight_layout()
plt.show()
