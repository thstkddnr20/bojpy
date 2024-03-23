# n, m = map(int, input().split(" "))
#
# answer = 1
#
# if n > 0 :
#     for i in range(n, 1, -1):
#         if i > m+1:
#             answer = answer * i
#         elif i == m+1:
#             pass
#         else :
#             answer = answer // i
#
# else :
#     print(0)
#     exit(0)
#
# answer_str = str(answer)
#
# cnt = 0
#
# for _ in range(len(answer_str)):
#     if answer % 10 == 0:
#         answer //= 10
#         cnt += 1
#     else:
#         break
#
# print(cnt)
n, m = map(int, input().split())
def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))