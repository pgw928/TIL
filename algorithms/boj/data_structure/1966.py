import sys
from collections import deque

input = sys.stdin.readline


T = int(input())


def solution(M, N, dq):

    count = 0
    while True:
        max_dq = max(dq)
        if max_dq != dq[0]:
            dq.rotate(-1)
            if M > 0:
                M -= 1
            else:
                M = N-1
        elif (max_dq == dq[M]) and (M==0):
            dq.popleft()
            count += 1
            break
        elif max_dq == dq[0]:
            dq.popleft()
            count += 1
            N -= 1
            M -= 1
    return count

for _ in range(T):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    print(solution(M, N, deque(A)))