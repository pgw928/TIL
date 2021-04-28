import sys; input = sys.stdin.readline
from collections import deque
graph = list(map(int, input().split())) + list(map(int, input().split())) + list(map(int, input().split()))
for i in range(9):
    if graph[i]==0:
        start = i
        graph[i] = 9
        break

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node):
    dq, visited = deque(), set()
    tmp = int(''.join(list(map(str, graph))))
    visited.add(tmp)
    dq.append((node,0, tmp))
    while dq:
        z, cnt, val = dq.popleft()
        if val == 123456789:
            return cnt
        y, x = z//3 , z%3
        # print('y, x :',y,x)
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<3 and 0<=a<3:
                # print('b, a :',b,a)
                # print(b*3 + a, z )
                n_z = b*3 + a 
                tmp = list(str(val))            
                tmp[n_z], tmp[z] = tmp[z], tmp[n_z]  
                n_val = int(''.join(tmp))
                if n_val not in visited:
                    visited.add(n_val)
                    dq.append((n_z, cnt+1, n_val))
    return -1
print(bfs(start))