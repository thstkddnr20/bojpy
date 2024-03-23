# num = int(input())
#
# answer = 0
# while num != 1:
#     # 3의 배수인지 확인
#     if num == 10:
#         answer += 3
#         break
#
#     if num % 3 == 0:
#         num //= 3
#         answer += 1
#
#     # 2의 배수인지 확인
#     elif num % 2 == 0:
#         num //= 2
#         answer += 1
#
#     # 둘다 아니라면 1을 뺀다
#     else:
#         num -= 1
#         answer += 1
#
# print(answer)

n = int(input())

# DP 테이블 초기화
d = [0] * (n + 1)

# 다이나믹 프로그래밍 진행(bottom-up)
for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

# 결과 출력
print(d[n])