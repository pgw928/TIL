import sys
from collections import deque

m_a, m_b, m_c = map(int, sys.stdin.readline())

def bfs(start):

    dq = deque()
    dq.append(start)
    check = set()
    while dq:
        a, b, c = dq.popleft()
        candi = [(a, b),(a,c),(b,c),(b,a),(c,a),(c,b)]
        max_val = [m_a, m_a, m_b, m_b, m_c, m_c]
        for i in range(6):
            x, y = candi[i]
            if x < max_val[i] and y>0:
                if (max_val[i]-x <= y) and (() not in check):
                    dq.append((m_a , b, c-m_a))
                    check.add(c-m_a)
                elif (0 not in check):
                    dq.append((a+c,b,0))
                    check.add(0)


bfs((0,0, m_c))