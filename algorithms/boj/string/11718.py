import sys
input = sys.stdin.readline
i = 0
while i<100:
    try:
        s = input().strip()
        print(s)
    except:
        break
    i += 1