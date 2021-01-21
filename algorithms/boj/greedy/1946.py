import sys
input = sys.stdin.readline
T = int(input())
# ----- main function -----
def sol(N):
    score = 0
    m = graph[0][1]
    for i in range(1,N):
        if m < graph[i][1]:
            score += 1
            print(f'i:{i}, min:{m}')
        m = graph[i][1]

    return N-score

# ----- solution -----
for _ in range(T):
    N = int(input())
    graph = [ tuple(map(int, input().split())) for _ in range(N)]
    graph.sort(key=lambda x: (x[0], x[1]))
    print(sol(N))

# 풀이 방법 : sorting (서류 성적, 면접 성적)  → 면접 성적만 비교
