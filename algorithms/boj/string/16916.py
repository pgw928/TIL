# import sys
#
# input1 = sys.stdin.readline().strip()
# input2 = sys.stdin.readline().strip()
#
# l1 = len(input1)
# l2 = len(input2)
#
# check = [0] * (l1+1)
# answer = 0
# j = 0
# while True:
#     for i in range(len(input2)):
#         if input1[j] == input2[i]:
#             check[j+1] = check[j]+1
#             j+=1
#         else:
#             j+=1
#             break
#     print(check, j, l2)
#     if check[j] == l2:
#         answer = 1
#         break
#     if j>=l1-l2+2:
#         break
# print(answer)

# 입력 : 패턴 문자열
# 반환 : lps 배열
def calcu_lps(pattern):

    lps = [0]*len(pattern)
    pattern_len = len(pattern)
    j = 0
    for i in range(1,len(pattern)):
        while (j > 0) and (pattern[i] != pattern[j]):
            j = lps[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
        else:
            j=0

    return lps

print(calcu_lps('ABABABABC'))