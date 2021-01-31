import sys

input = sys.stdin.readline

n = int(input())

i = n - (len(str(n))*9)+1
if i<10:
    print(0)
    exit()
while True:
    if sum(map(int, list(str(i)))) + i == n:
        print(i)
        break
    if i >= n:
        print(0)
        break
    i += 1