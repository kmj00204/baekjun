import sys

input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

dp = [[0 for _ in range(len(B))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            if 0 <= i - 1 < len(A) and 0 <= j - 1 < len(B):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

for a in dp:
    print(a)
print(max(val for row in dp for val in row))
