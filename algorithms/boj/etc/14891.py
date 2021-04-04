import sys; input = sys.stdin.readline
from collections import deque
top1 = deque(list(map(int, list(input().rstrip()))))
top2 = deque(list(map(int, list(input().rstrip()))))
top3 = deque(list(map(int, list(input().rstrip()))))
top4 = deque(list(map(int, list(input().rstrip()))))
# 0 : n극, 1: s극
k = int(input())
# 1 : 시계방향, -1 : 반시계
for _ in range(k):
    a, b = map(int, input().split())
    if a==1:
        if top1[2]==top2[6]:
            top1.rotate(b)
        else:
            top1.rotate(b)
            if top2[2]==top3[6]:
                top2.rotate(-b)
            else:
                top2.rotate(-b)
                if top3[2]==top4[6]:
                    top3.rotate(b)
                else:
                    top3.rotate(b)
                    top4.rotate(-b)
    if a==2:
        if top2[6]!=top1[2]:
            top1.rotate(-b)
        if top2[2]==top3[6]:
            top2.rotate(b)
        else:
            top2.rotate(b)
            if top3[2] == top4[6]:
                top3.rotate(-b)
            else:
                top3.rotate(-b)
                top4.rotate(b)
    if a==3:
        if top3[6]!=top2[2]:
            if top2[6]!=top1[2]:
                top1.rotate(b)
            top2.rotate(-b)
        if top3[2] == top4[6]:
            top3.rotate(b)
        else:
            top3.rotate(b)
            top4.rotate(-b)

    if a==4:
        if top3[2]==top4[6]:
            top4.rotate(b)
        else:
            top4.rotate(b)
            if top2[2]==top3[6]:
                top3.rotate(-b)
            else:
                top3.rotate(-b)
                if top2[6]==top1[2]:
                    top2.rotate(b)
                else:
                    top2.rotate(b)
                    top1.rotate(-b)

print(top1[0]*1+top2[0]*2+top3[0]*4+top4[0]*8)