a = int(input())

# array[1] = 1, array[2] = 2, array[3] = array[1] + array[2] ....

array = [0] * 1001

array[1], array[2] = 1, 2 # 1,2일 때는 고정값이다

for i in range(3, a+1):
    array[i] = array[i-2] + array[i-1]

print(array[a] % 10007)