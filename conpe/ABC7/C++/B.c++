#include<iostream>
#include<string>
using namespace std;

int main(void){
    string A;
    cin >> A;
    int N = A.length();
    if (N==1 && A[0]=='a')cout<<-1<<endl;
    else if (N==1)cout<<"a"<<endl;
    else{
        for (int i=1; i<N; i++)
        cout<<"a";
    }
    return 0;
}