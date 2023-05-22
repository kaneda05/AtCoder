#include<iostream>
#include<vector>
using namespace std;

int N, M;
int A[1000000], B[1000000];
vector<int> G[1000000];

int main(){
    cin >> N >> M;
    for (int i=1; i<=M; i++){
        cin >> A[i] >> B[i];
        G[A[i]].push_back(B[i]); // 頂点A[i]に隣接する頂点としてB[i]を追加
        G[B[i]].push_back(A[i]);
    }
    for (int i=1; i<=N; i++){
        cout << i << ": {";
        for (int j=0; j<G[i].size(); j++){
            if (1<=j) cout << ",";
            cout << G[i][j];
        }
        cout << "}" << endl;
    }
    return 0;
}