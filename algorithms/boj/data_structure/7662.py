import sys
import heapq
input = sys.stdin.readline
t = int(input())

check = [False]*1000001
for _ in range(t):
    k = int(input())
    min_Q, max_Q = [] , []

    for i in range(k):
        op, num = input().strip().split()
        if op == 'I':
            heapq.heappush(min_Q, (int(num), i))
            heapq.heappush(max_Q, (-int(num), i))
            check[i] = True
        elif min_Q:
            if num=='-1':
                while min_Q and not check[min_Q[0][1]]:
                    heapq.heappop(min_Q)
                if min_Q:
                    tmp = heapq.heappop(min_Q)
                    check[tmp[1]] = False
            else:
                while max_Q and not check[max_Q[0][1]]:
                    tmp = heapq.heappop(max_Q)
                if max_Q:
                    tmp = heapq.heappop(max_Q)
                    check[tmp[1]] = False

    while min_Q and not check[min_Q[0][1]]:
        heapq.heappop(min_Q)
    while max_Q and not check[max_Q[0][1]]:
        heapq.heappop(max_Q)
    print(f'{-max_Q[0][0]} {min_Q[0][0]}' if min_Q and max_Q else 'EMPTY')
