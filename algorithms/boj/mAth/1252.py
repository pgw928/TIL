import sys

a, b = map(int, sys.stdin.readline().split())
c = str(a + b)

result = ''
tmp = False
for x in c[::-1]:
    if x == '0':
        if tmp:
            result = '1' + result
            tmp = False
            continue
        result = x + result
    elif x == '1':
        if tmp:
            result = '0' + result
            continue
        result = x + result
    elif x == '2':
        if tmp:
            result = '1' + result
            continue
        result = '0' + result
        tmp = True
print(result if not tmp else '1' + result)