#값 입력받아 배열에 집어넣기
arr = []

for _ in range(9):
    arr.append(int(input()))

arr.sort()
arrSum = sum(arr)

# 값을 받아올곳
a, b = 0, 0

for i in range(8):
    for j in range(1+i, 9):
        if arrSum - arr[i] - arr[j] == 100:
            a = arr[i]
            b = arr[j]

arr.remove(a)
arr.remove(b)

for i in range(7):
    print(arr[i])

#9가지의 주어진 숫자를 다 더하고 2개를 빼서 100이 되면 된다. -> 2중 for문

