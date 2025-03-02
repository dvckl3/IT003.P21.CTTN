#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <sstream>

void process_test_cases(const std::string& input_file, const std::string& output_file) {
    std::ifstream in(input_file);
    std::ofstream out(output_file);
    std::string line;

    while (std::getline(in, line)) {
        if (line.empty()) continue;
        std::string test_case_name = line;
        std::vector<double> data;
        double num;

        std::getline(in, line);
        std::istringstream iss(line);
        while (iss >> num) {
            data.push_back(num);
        }

        // In ra thông tin test case trước khi sort
        std::cout << "Processing: " << test_case_name << " | Size: " << data.size() << std::endl;

        auto start = std::chrono::high_resolution_clock::now();
        std::sort(data.begin(), data.end());
        auto end = std::chrono::high_resolution_clock::now();
        double duration = std::chrono::duration<double, std::milli>(end - start).count();

        out << test_case_name << " " << duration << "ms\n";
    }
}

int main() {
    process_test_cases("all_testcases.txt", "cpp_sort.txt");
    return 0;
}
