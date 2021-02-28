import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    s, e = map(int, input().split())
    n = e - s
    bk_pt = False
    if n <=3:
        print(n)
    else:
        i = 2
        current = 2
        count = 2
        while True:
            for _ in range(2):
                count += 1
                current += i
                if n <= current:
                    print(count)
                    bk_pt= True
                    break
            i += 1
            if bk_pt:
                break
