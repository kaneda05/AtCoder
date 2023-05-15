#include <iostream>
#include <vector>
using namespace std;
int main(){
  string w;
  cin>>w;
  int n=w.length();
  for(int i=0;i<n;i++){
    if(w[i] !='a'&&w[i]!='u'&&w[i]!='o'&&w[i]!='i'&&w[i]!='e')cout<<w[i];
  }
  cout<<endl;
  return 0;
}
