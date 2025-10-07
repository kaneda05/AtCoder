#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        long long nA, nB, nC;
        cin >> nA >> nB >> nC;

        long long ans = min({nA, nC, (nA + nB + nC) / 3});
        cout << ans << "\n";
    }
    return 0;
}
