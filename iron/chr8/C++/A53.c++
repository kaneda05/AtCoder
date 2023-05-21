
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int Q;
int query[100009], x[100009];
priority_queue<int, vector<int>, greater<int> > T;

int main(){
    cin >> Q;
    for (int i=1; i<=Q; i++){
        cin >> query[i];
        if (query[i]==1) cin >> x[i];
    }

    for (int i=1; i<=Q; i++){
        if (query[i]==1) T.push(x[i]);
        if (query[i]==2) cout << T.top() << endl;  // 最小の要素を取得
        if (query[i]==3) T.pop(); // 最小の要素を削除
    }
    return 0;
}