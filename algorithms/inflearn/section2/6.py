import sys
sys.stdin = open('section2/input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))

# def digit_sum(x):
#     tmp = 0
#     for s in str(x):
#         tmp += int(s)
#     return tmp

def digit_sum(x):
    tmp = 0
    while x>0:
        tmp += x%10
        x //= 10
    return tmp



M, res = 0, 0
for a in arr:
    tot = digit_sum(a)
    if M > tot:
        M, res = tot, a
print(res)
