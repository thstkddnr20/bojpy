cnt = int(input())

for _ in range(cnt):
    a, b = map(int, input().split(" "))

    if b > a :
        a, b = b, a

    d, e = a, b

    if b == 0:
        print(0)

    while b != 0:
        a, b = b, a % b

    print(d * e // a)



