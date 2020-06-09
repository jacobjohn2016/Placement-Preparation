#include <bits/stdc++.h>

using namespace std;

int main() {
	int t, n, s, cumsum, i, x;

    cin >> t;
    while(t--){
        cumsum = 0;
        
        cin >> n >> s;
        int a[n];

        for(i = 0; i < n; i++)
            cin >> a[i];

        deque <int> Q;

        for(i = 0; i < n; i++){
            if(s > cumsum){
                Q.push_back(i);
                cumsum += a[i];
            }
            while(s < cumsum){
                cumsum -= a[Q.front()];
                Q.pop_front();
            }
            if(cumsum == s)
                break;
        }

        if(Q.empty() || cumsum != s)
            cout << -1 << endl;
        else
            cout << Q.front() + 1 << " " << Q.back() + 1 << endl;
    }

	return 0;
}