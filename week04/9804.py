import sys

input = sys.stdin.readline


def fun():
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    # arr = [0 for _ in range(target + 1)]
    # arr[0] = 1
    #
    # for coin in coins:
    #     for i in range(coin, target + 1):
    #         if 0 <= i - coin < target + 1:
    #             arr[i] += arr[i - coin]
    # print(arr[target])

    dp = [[0 for _ in range(target + 1)] for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        coin = coins[i - 1]
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= coin:
                dp[i][j] += dp[i][j - coin]

    print(dp[N][target])


T = int(input())

for _ in range(T):
    fun()
