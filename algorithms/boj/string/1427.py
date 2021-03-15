import sys
st = sorted(list(map(int, list(sys.stdin.readline().strip()))), reverse=True)
print(''.join(list(map(str, st))))