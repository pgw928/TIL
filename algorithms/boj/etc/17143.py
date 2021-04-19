import sys; input = sys.stdin.readline
r, c, m = map(int, input().split())

shark = dict()
for _ in range(m):
    tmp = tuple(map(int, input().split()))
    shark[tmp[:2]] = tmp[2:]

def move(shark):
    tmp = dict()
    for (b, a) in shark:
        v, d, s = shark[(b, a)]
        t = v
        while t:
            if d==1:  # 위로
                if t//(2*(r-1)) > 0:
                    t%=(2*(r-1))
                if t < b-1:
                    b -= t
                    break
                elif t < b-2+r :
                    d = 2
                    b = 1 + (t - (b-1))
                    break
                else:
                    b = r-(t-b+2-r)
                    break
            elif d == 2:
                if t // (2 * (r - 1)) > 0:
                    t %= (2 * (r - 1))
                if t < r - b:
                    b += t
                    break
                elif t < 2 * r - b -1:
                    d = 1
                    b = r - (t - (r - b))
                    break
                else:
                    b = 1 + (t - 2 * r + b+1)
                    break
            elif d == 3:
                if t // (2 * (c - 1)) > 0:
                    t %= (2 * (c - 1))
                if t < c - a:
                    a += t
                    break
                elif t < 2 * c - a - 1:
                    d = 4
                    a = c - (t - (c - a))
                    break
                else:
                    a = 1 + (t - 2 * c + a + 1)
                    break
            elif d == 4:
                if t // (2 * (c - 1)) > 0:
                    t %= (2 * (c - 1))
                if t < a - 1:
                    a -= t
                    break
                elif t < a - 2 + c:
                    d = 3
                    a = 1 + (t - (a - 1))
                    break
                else:
                    a = c - (t - a + 2 - c)
                    break

        if (b, a) not in tmp:
            tmp[(b, a)] = v, d, s
        else:
            v1, d1, s1 = tmp[(b, a)]
            if s > s1:
                tmp[(b,a)] = v, d, s
    return tmp

i, score = 1, 0
while i <= c:
    for j in range(1, r+1):
        if (j, i) in shark:
            score += shark[(j, i)][2]
            del shark[(j, i)]
            break
    shark = move(shark)
    i += 1

print(score)