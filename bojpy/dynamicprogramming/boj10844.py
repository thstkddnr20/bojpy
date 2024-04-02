N = int(input())

dp = [1 for _ in range(N+1)]

dp[1] = 9

if N == 1:
    print(9)
    exit(0)

for i in range(2, N+1):
    dp[i] = (dp[i-1] * 2 - (i-1)) % 1000000000

print(dp[N])