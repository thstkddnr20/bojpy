n = int(input())

array = [0] * 1001

array[1], array[2] = 1, 3 # 1,2일 때는 고정값이다

for i in range(3, n+1):
    array[i] = 2 * array[i-2] + array[i-1]
    #로직
    array[i] %= 10007

print(array[n])