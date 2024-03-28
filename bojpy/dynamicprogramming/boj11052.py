#카드개수 입력받기
cnt = int(input())

# 카드의 가격들 입력받기
p = list(map(int, input().split(" ")))
p.insert(0, 0)

dp = [0 for _ in range(cnt+1)]

for i in range(1, cnt +1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j] + p[j], dp[i])

print(dp[cnt])


"""
4
dp = 0, 0, 0, 0, 0
p = [0, 1, 5, 6, 7]

dp[1] = 1
dp[2] = dp[2-1] + p[1], dp[2]중 큰 것
dp[3] = dp[2]+p[1], dp[1]+p[2], dp[3]중 큰것
dp[4] = 
"""