import sys

input = sys.stdin.readline
T = int(input())


# ----- main function -----
def sol(N):
    m = graph[1]
    score = 0
    for i in range(2, N + 1):
        if m < graph[i]:
            score += 1
        else:
            m = graph[i]

    return N - score


# ----- solution -----
for _ in range(T):
    N = int(input())
    graph = [0] * (N + 1)
    for _ in range(N):
        a, b = tuple(map(int, input().split()))
        graph[a] = b
    print(sol(N))
