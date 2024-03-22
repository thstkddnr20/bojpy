a = input()

lst = [0 for _ in range(26)]

for i in range(0, len(a)):
    asciii = ord(a[i]) - 97
    lst[asciii] += 1


output = ' '.join(map(str, lst))
print(output)