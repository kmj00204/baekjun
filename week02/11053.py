n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    maxlong = 0
    maxidx = False
    for j in range(0, i):
        if maxlong < dp[j] and arr[j] < arr[i]:
            maxlong = dp[j]
            maxidx = j
    if maxidx is not False:
        dp[i] = dp[maxidx] + 1
    else:
        dp[i] = 1

print(max(dp))
