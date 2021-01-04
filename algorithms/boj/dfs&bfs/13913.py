import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0]*(10**5+1)
where = [-1]*(10**5+1)


def bfs(start_node, end_node):
    dq = deque()
    dq.append(start_node)
    visited[start_node] = 1
    # print(start_node)
    while dq:
        node = dq.popleft()
        if node == end_node:
            return visited[end_node]-1
        for n_node in [node-1, node+1, 2*node]:
            if 0<=n_node<=10**5 and visited[n_node]==0:
                visited[n_node] = visited[node]+1
                where[n_node] = node
                dq.append(n_node)

def make_path(where, K):
    i = K
    result = [K]
    while where[i] != -1:
        i = where[i]
        result.append(i)
    return ' '.join(map(str,result[::-1]))


print(bfs(N, K))
print(make_path(where, K))



