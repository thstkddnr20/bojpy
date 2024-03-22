cnt = int(input())

lst = list(map(int, input().split(" ")))

resultNum = 0
for num in lst:
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break

        if count == 0:
            resultNum += 1


print(resultNum)