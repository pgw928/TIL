import sys

F, S ,G, U, D = map(int, sys.stdin.readline().split())

# 총 F층
# 스타트링크 G층
# 강호 S층
# 엘베 G층으로 이동

# 버튼 2개 U, d

def bfs(start_node, end_node, F, U, D):
    q, check =[], [0]*(F+1)
    q.append(start_node)
    check[start_node] = 1
    for node in q:
        if node == end_node:
            return check[node]-1
        if (1<=node+U<=F) and check[node+U]==0:
            check[node+U] = check[node]+1
            q.append(node+U)
        if (1 <= node - D <= F) and check[node - D] == 0:
            check[node - D] = check[node] + 1
            q.append(node - D)
    return 'use the stairs'

print(bfs(S, G, F, U, D))

