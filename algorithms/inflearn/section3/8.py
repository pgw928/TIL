import sys
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
l = n//2

def count(graph):
    cnt = 0
    for i in range(n):
        if i<=l:
            for j in range(i, n-i):
                cnt += graph[i][j] 
        else:
            for j in range(n-i-1, i+1):
                cnt += graph[i][j]
    return cnt

for _ in range(m):
    a, b, c = map(int, input().split())
    c %= n 
    a -= 1
    if b==0:
        graph[a] = graph[a][c:] + graph[a][:c]
    else:
        graph[a] = graph[a][-c:] + graph[a][:-c]

print(count(graph))