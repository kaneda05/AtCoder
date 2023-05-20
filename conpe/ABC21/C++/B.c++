#include<iostream>
#include<set>
#include<vector>

using namespace std;

int main(){
    int N,a,b,K;
    cin >> N >> a >> b >> K;

    set<int> S; // setの定義
    S.insert(a); // setへ追加
    S.insert(b);

    for (int i=0; i<K; i++){
        int P;
        cin >> P;
        S.insert(P);
    }

    if (S.size()==K+2) cout << "YES" << endl;
    else cout << "NO" << endl;
}