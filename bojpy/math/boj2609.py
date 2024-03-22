a, b = map(int, input().split(" "))

# a가 큰 수 b가 작은수
if (b > a):
    a, b = b, a

#기존의 a,b를 기억할 변수
d = a
e = b

# 입력된 값 중 하나가 0인 경우 다른 값이 최대공약수가 됨
if b == 0:
    print(a)
    print(0)
    exit(0)

while b != 0:
    a, b = b, a % b

print(a)
print(d * e // a)
