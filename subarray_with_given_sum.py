#Subarray with given sum using sliding window
def subarray(arr, n, s):
    i = 0
    j = 1
    currsum = arr[i] + arr[j]
    while(i != n-1 and j != n-1):
        if s == currsum:
            return i, j
        while(s < currsum):
            currsum = currsum - arr[i]
            i = i + 1
        j = j + 1
        currsum = currsum + arr[j]
    return -1, -1


t = int(input())
for i in range(t):
    n, s = input().split()
    n = int(n)
    s = int(s)
    arr = input().split()
    for j in range(n):
        arr[j] = int(arr[j])
    a, b = subarray(arr, n, s)
    if(a == -1 and b == -1):
        print(-1)
    else:
        print(a+1, b+1)