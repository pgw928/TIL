import sys; input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
M = 1_000_000
visited = [[0]*(M+1) for _ in range(2)]

def bfs(n):
    dq = deque()
    dq.append((str(n), 0))
    while dq:
        print(dq)
        x, z = dq.popleft()
        if z==k:
            continue
        for i in range(len(x)-1):
            for j in range(i+1, len(x)):
                if i==0 and x[j]=='0':
                    continue
                if j<len(x)-1 :
                    y = x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
                    if int(y)<= M and visited[(z+1)%2][int(y)]==0:
                        dq.append((y, z+1))
                        visited[(z+1)%2][int(y)] = 1
                elif j==len(x)-1:
                    y = x[:i]+x[j]+x[i+1:j]+x[i]
                    if int(y)<= M and visited[(z+1)%2][int(y)]==0:
                        dq.append((y, z+1))
                        visited[(z+1)% 2][int(y)] = 1
    if k%2==0:
        tmp = [i for i in range(M+1) if visited[0][i]>0 ]
        return max(tmp) if tmp else -1
    if k%2==1:
        tmp = [i for i in range(M+1) if visited[1][i]>0 ]
        return max(tmp) if tmp else -1
print(bfs(n))

# if len(str(n))>1:
# else:
#     print(-1)