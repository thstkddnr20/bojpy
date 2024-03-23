a = int(input())

answer = 1

if a > 0 :
    for i in range(1, a+1):
        answer = answer * i

answer_str = str(answer)

cnt = 0

for _ in range(len(answer_str)):
    if answer % 10 == 0:
        answer //= 10
        cnt += 1
    else:
        break

print(cnt)