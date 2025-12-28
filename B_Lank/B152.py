N, X = map(int, input().split())

v = list(map(int, input().split()))
a = list(map(int, input().split()))

NEG_INF = -10**18
dp = [NEG_INF] * (X + 1)
dp[0] = 0

for i in range(N):
    price = v[i]
    satis = a[i]

    for money in range(X - price, -1, -1):
        if dp[money] != NEG_INF:
            dp[money + price] = max(dp[money + price], dp[money] + satis)

print(dp[X])