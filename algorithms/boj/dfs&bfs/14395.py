import sys
from collections import deque

input = sys.stdin.readline
s, t = map(int, input().split())

where = {}
def make_result(end_node):
    tmp = end_node
    result = ''
    while True:
        if tmp in where:
            result += where[tmp][1]
            tmp = where[tmp][0]
        else:
            return result[::-1]


check = []
def bfs(start_node, end_node):

    dq = deque()
    dq.append(start_node)
    check.append(start_node)
    while dq:
        node = dq.popleft()

        if node == end_node:
            return make_result(end_node)
        for n_node in [node**2, 2*node, 0, 1]:
            if n_node == end_node:
                if n_node == 0:
                    where[n_node] = (node,'-')
                elif n_node == 1:
                    where[n_node] = (node,'/')
                elif n_node == node**2:
                    where[n_node] = (node, '*')
                else:
                    where[n_node] = (node, '+')
                return make_result(end_node)
            if (n_node not in check) and n_node < end_node:
                check.append(n_node)
                if n_node == 0:
                    where[n_node] = (node, '-')
                elif n_node == 1:
                    where[n_node] = (node, '/')
                elif n_node == node ** 2:
                    where[n_node] = (node, '*')
                else:
                    where[n_node] = (node, '+')
                dq.append(n_node)
    return -1


if s==t:
    print(0)
else:
    print(bfs(s,t))



