#include <iostream>
#include <string>
#include <map>
using namespace std;

int Q;
int query[100009], y[100009];
string x[100009];
map<string, int> Map;

int main(){
    cin >> Q;
    for (int i=1; i<=Q; i++){
        cin >> query[i];
        if (query[i]==1) cin >> x[i] >> y[i];
        if (query[i]==2) cin >> x[i];
    }

    for (int i=1; i<=Q; i++){
        if (query[i]==1) Map[x[i]]=y[i];
        if (query[i]==2) cout << Map[x[i]] << endl;
    }
    return 0;
}