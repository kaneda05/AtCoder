#include <iostream>
#include <vector>
using namespace std;
int main(){
  int N;
  int ans;
  cin>>N;
  for (int i=1;i<=N;i++){
      ans += i*10000;
  }
  ans/=N;
  cout << ans << endl;
  return 0;

}

