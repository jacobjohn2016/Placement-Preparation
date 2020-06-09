## Subarray with given sum
Source: [GeeksforGeeks](https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0)

We need to use Sliding window Method to solve this Problem.

Add the elements, to currsum till it is less than S. If it becomes more than S, start deleting elements from start in the cuusum. if the currsum again becomes less than S, again start adding elements to it. In between also check, if the currsum becomes equal to S.
If yes, then output start and end index, else after traversing array no such solution is found, output -1.

``` cpp
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
```

### Deque

* similar to vectors, but are more efficient in case of insertion and deletion of elements
* Unlike vectors, contiguous storage allocation may not be guaranteed
* implementation of the data structure double ended queue

Example:

``` cpp
void showdq(deque <int> g) 
{ 
    deque <int> :: iterator it; 
    for (it = g.begin(); it != g.end(); ++it) 
        cout << '\t' << *it; 
    cout << '\n'; 
} 

int main(){
    deque <int> gquiz; 
    gquiz.push_back(10); 
    gquiz.push_front(20); 

    cout << "The deque gquiz is : "; 
    showdq(gquiz); 

    cout << "\ngquiz.size() : " << gquiz.size(); 
    cout << "\ngquiz.max_size() : " << gquiz.max_size(); 

    cout << "\ngquiz.at(2) : " << gquiz.at(2); 
    cout << "\ngquiz.front() : " << gquiz.front(); 
    cout << "\ngquiz.back() : " << gquiz.back(); 

    cout << "\ngquiz.pop_front() : "; 
    gquiz.pop_front(); 
    showdq(gquiz); 

    cout << "\ngquiz.pop_back() : "; 
    gquiz.pop_back(); 
    showdq(gquiz);
} 
```

### References

1. [GFG - Deque C++ STL](https://www.geeksforgeeks.org/deque-cpp-stl/)
