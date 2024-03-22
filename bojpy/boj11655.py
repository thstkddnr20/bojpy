# 인풋
a = input()
lst = []


# for문으로 0부터 개수까지 돌리기
for i in range(0, len(a)):

    if (a[i] == ' ' or ord(a[i]) < 65):
        lst.append(a[i])

    else :
        ascii = ord(a[i])
        # 대문자인경우
        if ascii < 97:
            ans = ascii + 13
            if ans > 90 :
                lst.append(chr(ans - 26))
            else :
                lst.append(chr(ans))

        else:
            ans = ascii + 13
            if ans > 122:
                lst.append(chr(ans - 26))
            else :
                lst.append(chr(ans))





    # 공백인지, 숫자인지 확인
    # 소문자, 대문자일 경우
    # 아스키코드를 13더해서 기존 문자열에 바꾸기


print(''.join(lst))
