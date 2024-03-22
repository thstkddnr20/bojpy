a = input()
lst = [char for char in a]
anslst = []

 # 처음 값 넣어주고 시작
for i in range(len(a)):
    anslst.append(''.join(lst))
    if len(lst) > 0:
        lst.pop(0)

anslst.sort()
for j in range(len(anslst)):
    print(anslst[j])