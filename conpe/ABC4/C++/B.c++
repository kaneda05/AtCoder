#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
int main(){
    char c[5][5];
    for (int i=1;i<=4;i++){
        for (int j=1;j<=4;j++)cin>>c[i][j];
    }
    for (int i=4;1<=i;i--){
        for (int j=4;1<=j;j--)cout<<c[i][j]<<' ';
        cout<<'\n';
    }
}

