ans = ''
numbers = [3, 30, 34, 5, 9, 35, 37, 33, 31,32,0]
n_l = list(map(str,numbers))

my_list = []

for k in range(9,-1,-1):
    temp = [n for n in n_l if int(n[0])==k]
    if temp :
        my_list.append(temp)
print(my_list)

def rel_nums(a,b):
    if int('a'+'b') > int('b'+'a'):
        return ['a','b']
    else :
        return ['b','a']

for lst in my_list:
    for n in range(0,len(lst)):



# def rel_nums(a,b):
#     k = 0
#     s_a = str(a); l_a = len(s_a)
#     s_b = str(b); l_b = len(s_b)
#     l = min(l_a, l_b)
#     if l_a>l_b:
#         flag = 0
#     elif l_a<l_b:
#         flag = 1
#     else:
#         flag = 2
#
#     if flag == 2 :
#         while True:
#             if s_a[k] > s_b[k]:
#                 return [a,b]
#             elif s_a[k] < s_b[k]:
#                 return [b,a]
#             else:
#                 k += 1
#             if k==l:
#                 return [a, b]
#
#     elif flag == 1 :
#         while True:
#             if s_a[k] > s_b[k]:
#                 return [a, b]
#             elif s_a[k] < s_b[k]:
#                 return [b, a]
#             else:
#                 k += 1
#             if k == l:
#                 if s_b[k] >= s_a[k-1]:
#                     return [b, a]
#                 else:
#                     return [a, b]
#     else:
#         while True:
#             if s_a[k] > s_b[k]:
#                 return [a, b]
#             elif s_a[k] < s_b[k]:
#                 return [b, a]
#             else:
#                 k += 1
#             if k==l:
#                 if s_a[k] >= s_b[k-1]:
#                     return [a, b]
#                 else:
#                     return [b, a]

print(rel_nums(25,254))
print('30'>'254')
