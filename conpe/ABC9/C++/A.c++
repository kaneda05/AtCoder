#include <iostream>
#include <vector>
using namespace std;
int main(){
    int N;
    int cnt = 0;
    cin >> N;
    while (0 < N){
        N-= 2;
        cnt += 1;
    }
    cout << cnt << endl;
    return 0;
}