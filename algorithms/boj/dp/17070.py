import sys; input = sys.stdin.readline
n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]
A, B, C = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]

for i in range(1, n):
    if graph[0][i] == 1:
        break
    A[0][i] = 1

for i in range(1,n):
    for j in range(2,n):
        if graph[i][j]==0:
            A[i][j] = A[i][j-1]  + C[i][j-1]
            B[i][j] = B[i-1][j] + C[i-1][j]
            if graph[i-1][j]==0 and graph[i][j-1]==0:
                C[i][j] = A[i-1][j-1] +B[i-1][j-1] + C[i-1][j-1]

print(A[-1][-1]+B[-1][-1]+C[-1][-1])