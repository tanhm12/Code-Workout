#include <iostream>
#include <vector>
using namespace std;

#define ll long long

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, v;
    cin >>n>>v;

    ll temp;
    ll acc[n+1];
    acc[0] = 0;
    for ( int i =1 ; i <= n; ++i){
        cin >> temp;
        acc[i] = acc[i-1] + temp;
    }

    ll res = 0;
    int mark = 1;
    for (int i= 1; i <=n ; ++i){
        temp = acc[i-1] + v;
        while (mark <= n && acc[mark] < temp){
            mark++;
        }
        if (mark <= n){
            res += n + 1 - mark;
        } else{
            break;
        }
    }
    cout << res;
    return 0;
}