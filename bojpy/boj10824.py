a = input().split()
# 1 2 3 4 입력받으면
# input.split() = ['1', '2', '3', '4']
# map하면 [1, 2, 3, 4] int로 변환

str1 = a[0] + a[1]
str2 = a[2] + a[3]

int1 = int(str1)
int2 = int(str2)

print(int1 + int2)


