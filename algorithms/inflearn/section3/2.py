# import sys
# sys.stdin = open('section3/input.txt', 'rt')
# st = input().rstrip()

# def num_of_divisor(n):
#     cnt = 2
#     for i in range(2, n//2+1):
#         if n%i==0:
#             cnt += 1
#     return cnt

# n = int(''.join([s for s in st if s.isnumeric()]))
# print(n)
# print(num_of_divisor(n))

#----------------------------
import sys
sys.stdin = open('section3/input.txt', 'rt')
st = input().rstrip()

def num_of_divisor(n):
    cnt = 2
    for i in range(2, n//2+1):
        if n%i==0:
            cnt += 1
    return cnt

res = 0
for  x in st:
    if x.isdecimal():
        res = 10*res + int(x)
print(res)
print(num_of_divisor(res))