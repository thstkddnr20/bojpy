# 소문자
# 대문자
# 숫자
# 공백

# while True:
#     try:
#         a = input()
#         lst = [0,0,0,0]
#
#         for i in range(0, len(a)):
#             if ord(a[i]) >= 97:
#                 lst[0] += 1
#
#             elif ord(a[i]) >= 65:
#                 lst[1] += 1
#
#             elif ord(a[i]) >= 49:
#                 lst[2] += 1
#
#             else:
#                 lst[3] += 1
#
#         output = ' '.join(map(str, lst))
#         print(output)
#
#     except EOFError:
#         break
while True :
    try :
        text_lst = list(input())
        lower , upper, num, blank = 0,0,0,0
        for i in range(len(text_lst)) :
            if text_lst[i] == " " :
                blank += 1
            elif 65 <= ord(text_lst[i]) <= 90 :
                upper += 1
            elif 97 <= ord(text_lst[i]) <= 122 :
                lower += 1
            else :
                num += 1
        print(lower,upper,num,blank)
    except EOFError :
        break

