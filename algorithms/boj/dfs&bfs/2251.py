import sys
from collections import deque


max_A = 8
max_B = 9
max_C = 10
visited = [-1]*(max_C+1)

# 전부 쏟아 부운다.
# 하나가 다 찰때까지 부운다.
def bfs(start_node):
    dq = deque()
    dq.append(start_node)
    result = [start_node[2]]
    visited[start_node[2]] = 0
    while dq:
        a,b,c = dq.popleft()
        for i in range(6):
            if i == 0:
                if (max_A-a)>=c:
                    a =+c
                    c = 0
                elif (max_A-a)<c:
                    a = max_A
                    c = c- max_A+a
            elif i ==1:
                if (max_A - a) >= c:
                    a = +c
                    c = 0
                elif (max_A - a) < c:
                    a = max_A
                    c = c - max_A + a

