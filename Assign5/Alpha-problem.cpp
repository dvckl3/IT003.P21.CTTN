#include <bits/stdc++.h>
#include <string>
using namespace std;

string convert_base(unsigned long long a, int x) {
    if (a == 0) return "0";
    string result = "";
    while (a > 0) {
        result = char('0' + a % x) + result;
        a /= x;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    unsigned long long a;
    int x;
    cin >> a >> x;
    cout << convert_base(a, x) << endl;
    return 0;
}
