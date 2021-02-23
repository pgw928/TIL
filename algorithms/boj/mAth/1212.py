import sys
num = '0o' + sys.stdin.readline().strip()
print(int(num, 8))
print(format(int(num, 8), 'b'))