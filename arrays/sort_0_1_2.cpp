#include <bits/stdc++.h>

using namespace std;

void quicksort(int *a, int low, int high){
    int i;
    
}

int main(){
    int t, n, i;
    cin >> t;
    while(t--){
        cin >> n;
        int a[n];
        for(i = 0; i < n; i++)
            cin >> a[i];

        quicksort(a, 0, n-1);

        for(i = 0; i < n; i++)
            cout << a[i] << " ";
        cout << endl;
    }
}