# # # front_v, back_v = input('입력 예시: 1.0.0 1.0.23').split()
# # # f, b = front_v.split('.'), back_v.split('.')
# # # best_len = 0
# # # if len(f)>len(b):
# # #     best_len = len(f)
# # # else:
# # #     best_len = len(b)
# # # for i in range(best_len):
# # #     if(f[i]>b[i]):
# # #         print(front_v,'>', back_v)
# # #     elif(f[i]<b[i]):
# # #         print(back_v, '<', front_v)
# # #
# #
# # # num1, num2 = map(int, input().split())
# # # sum = 0
# # # for i in range(num1, num2+1):
# # #     text = ''
# # #     for j in str(i):
# # #         if(j != '0'):
# # #             text += j+'*'
# # #         else:
# # #             text += '0*'
# # #     print(text[:-1])
# # #     sum += eval(text[:-1])
# # # print(sum)
# #
# # name = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
# #
# # # 1)김씨와 이씨는 각각 몇 명 인가요?
# # # 2)"이재영"이란 이름이 몇 번 반복되나요?
# # # 3)중복을 제거한 이름을 출력하세요.
# # # 4)중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
# #
# # lst_name = name.split(',')
# # print(lst_name)
# # #1)
# # import re
# # name_kim = re.findall("[김][\D]{2}", name)
# # name_lee = re.findall("[이][\D]{2}", name)
# # print('김씨와 이씨는 각각 {},{}명이다.'.format(len(name_kim),len(name_lee)))
#
# ver1, ver2 = "1.0.75", "1.0.23"
#
# def compare_ver(ver1, ver2):
#     if ver1 > ver2:
#         print("{0} > {1}".format(ver1, ver2))
#     else:
#         print("{1} > {0}".format(ver1, ver2))
#
# compare_ver(ver1, ver2)


print("1.0.9">"1.0.12")

print("29">"12")





num1, num2 = "10", "15"
hop = []
for i in range(int(num1), int(num2)+1):
    gop = 1
    for j in str(i)[:]:
        gop *= int(j)
    hop.append(gop)
print(sum(hop))