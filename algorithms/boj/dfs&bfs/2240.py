import sys
from collections import deque
input = sys.stdin.readline

t, w = map(int, input().split())
A = [int(input()) for _ in range(t)]

dp = [0]*(t+1)
def bfs():
    dq = deque()
    dq.append((0, -1, 1, 0)) # 개수, 시간, 위치, 바꾼 횟수
    result = set()
    position = {2:1, 1:2}
    while dq:
        a, b, c, d = dq.popleft()
        if b == t-1:
            result.add(a)
        else:               # 마지막 열매가 아니면
            if c==A[b+1]:   # 현재 위치랑 같다면
                dq.append((a+1, b+1, c, d))
            else:           # 현재 위치랑 다르면
                dq.append((a, b+1, c, d)) # 위치 안바꿈
                if d<w:  # 바꿀 힘이 있다면
                    dq.append((a+1, b+1, position[c],d+1))
    return result

print(max(bfs()))