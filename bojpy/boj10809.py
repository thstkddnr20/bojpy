a = input()

lst = [-1 for _ in range(26)]

for i in range(0, len(a)):
    asciii = ord(a[i]) - 97
    if lst[asciii] == -1:
        lst[asciii] = i

output = ' '.join(map(str, lst))
print(output)