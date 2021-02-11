import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tmp = [ list(input().strip()) for _ in range(n)]
graph = {i:[] for i in range(n)}
no_graph = {i:[] for i in range(n)}

for i in range(1,n):
    for j in range(i):
        if tmp[i][j]=='Y':
            graph[i].append(j)
            graph[j].append(i)
        else:
            no_graph[i].append(j)
            no_graph[j].append(i)

result = [0]* n

def sol(start):
    node = start
    for no_friend in no_graph[node]:
        for friend in graph[node]:
            if no_friend in graph[friend]:
                print(friend, no_friend)
                result[node] += 1
                break

for i in range(n):
    result[i] = len(graph[i])
    sol(i)
print(max(result))
