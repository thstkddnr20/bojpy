#카드개수 입력받기
cnt = int(input())

# 카드의 가격들 입력받기
p = list(map(int, input().split(" ")))
p.insert(0, 0)

dp = [0 for _ in range(cnt+1)]

dp[1] = p[1]

for i in range(2, cnt +1):
    dp[i] = p[i]
    for j in range(1, i+1):
        dp[i] = min(dp[i-j] + p[j], dp[i])


print(dp[cnt])