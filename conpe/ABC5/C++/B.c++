#include <iostream>
#include <vector>
using namespace std;
int main(){
  int N;
  vector<int> t(N);
  cin >> N;
  int minT = 1000000;

  for (int i=0;i<N;i++){
      cin >> t[i];
  }

  for (int i=0;i<N;i++){
      if (t[i]<minT){
          minT=t[i];
      }
  }

  cout<<minT<<endl;

  return 0;

}