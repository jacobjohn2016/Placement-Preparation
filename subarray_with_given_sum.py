#Subarray with given sum using sliding window
def subarray(arr, n, s):
    start = 0
    end = 1
    currsum = arr[start] + arr[end]
    while(start != n and end != n):
        if s == currsum:
            return start, end
        elif(s > currsum):
            end = end + 1
            if(end == n):
                continue
            currsum = currsum + arr[end]
        # keep subtracting until currsum is less than desired sum
        elif(s < currsum):
            currsum = currsum - arr[start]
            start = start + 1
    return -1, -1

testcase = int(input())
for i in range(testcase):
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
