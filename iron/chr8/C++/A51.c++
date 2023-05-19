#include <iostream>
#include <stack>
#include <string>

using namespace std;

int Q;
int Querys[100009]; string x[100009];
stack<string> S;

int main(){
    cin >> Q;
    for (int i=1; i<=Q; i++){
        cin >> Querys[i];
        if (Querys[i] == 1) cin >> x[i];
    }

    // クエリ処理
    for (int i=1; i<=Q; i++){
        if (Querys[i]==1) S.push(x[i]);
        if (Querys[i]==2) cout << S.top() << endl;
        if (Querys[i]==3) S.pop();
    }

    return 0;
}