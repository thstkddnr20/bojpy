a = int(input())

answer = 1

if a > 0 :
    for i in range(1, a+1):
        answer = answer * i
    print(answer)
else:
    print(1)