import sys
from collections import deque

input = sys.stdin.readline

s, t = map(int, input().split())
check = {}
def bfs(start_node, end_node):


    result = []

    dq = deque()
    dq.append(start_node)
    check[start_node] = 1
    while dq:
        print(dq)
        node = dq.popleft()

        if node == end_node:
            return result
        if not node:
            for n_node in [node**2, 2*node, 0, 1]:
                if n_node == end_node:
                    check[n_node] = check[node] + 1
                    return result
                if not check.get(n_node, 0):
                    check[n_node] = check[node] + 1
                    dq.append(n_node)
        else:
            for n_node in [node ** 2, 2 * node, 0]:
                if n_node == end_node:
                    check[n_node] = check[node] + 1
                    return result
                if not check.get(n_node, 0):
                    check[n_node] = check[node] + 1
                    dq.append(n_node)
    return -1

bfs(s, t)

print(check)
if s==t:
    print(0)

n = check[t]
cur = t
while True:
    if (cur*cur in check) and (check[cur*cur]== n-1):
        n = check[cur]
        cur = cur*cur
    elif (int(cur**(1/2)) in check) and (check[cur*cur]== n-1):
        
    elif (cur + cur in check)  and (check[cur*cur]== n-1):

    elif 0 in check and check[0] == n-1:
