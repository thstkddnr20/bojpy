import math

for i in range(100001):
    a = int(input())
    if a == 0: #마지막 줄에는 0
        exit(0)

    if a % 2 != 0 or a < 5: #4보다 작은 경우는 안됨
        print("Goldbach's conjecture is wrong.")
        continue

    case = [True for i in range(a+1)]

    for i in range(2, int(math.sqrt(a)) + 1):
        if case[i] == True:
            j = 2
            while i * j <= a:
                case[i * j] = False
                j += 1

    cnt = 0
    for i in range(len(case)-1, 0, -1):
        if case[i] == True:
            cnt += 1
        if cnt == 2:
            cnt = i
            break

    print(f"{a} = {a-cnt} + {cnt}")


# 새로운 풀이
import sys

number = [True] * 1000001

# 소수 list
for i in range(2, int(len(number) ** 0.5) + 1):
    if number[i]:
        for j in range(2 * i, 1000001, i):
            number[j] = False


while 1:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if (number[i] == True) and (number[n - i] == True):
            print(f"{n} = {n-i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')



#모든 접근방식은같지만 미리 1000001개의 테스트케이스를 만들어놓고 찾는다는 점에서 다르다