import math

a, b = (map(int, input().split(" ")))

#에라토스테네스의 체

array = [True for i in range(b + 1)] # 인덱스 2부터 2다.

for i in range(2, int(math.sqrt(b)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= b:
            array[i * j] = False
            j += 1

for i in range(a, b + 1):
    if array[i] and i > 1:
        print(i)