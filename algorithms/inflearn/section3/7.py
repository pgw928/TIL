import sys
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

score = 0
l = n//2
for i in range(l+1):
    score += ( sum(graph[i][l:l+1+i]) + sum(graph[i][l-i:l]) )

for i in range(l+1, n):
    score += ( sum(graph[i][l:n+l-i]) + sum(graph[i][i-l:l]) )

print(score)    