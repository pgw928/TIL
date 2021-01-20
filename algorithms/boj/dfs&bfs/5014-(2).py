import sys

F, S ,G, U, D = map(int, sys.stdin.readline().split())

# 총 F층
# 스타트링크 G층
# 강호 S층
# 엘베 G층으로 이동

# 버튼 2개 U, d

def bfs(start_node, end_node, F, U, D):
    q, check = [(start_node, 0)], set()
    check.add(start_node)

    for node,result in q:
        if node == end_node:
            return result
        if (1<=node+U<=F) and ((node+U) not in check):
            check.add(node+U)
            q.append((node+U,result+1))
        if (1 <= node - D <= F) and ((node-D) not in check):
            check.add(node-D)
            q.append((node - D, result+1))
    return 'use the stairs'

print(bfs(S, G, F, U, D))

