import sys

input = sys.stdin.readline
t = int(input())
memo = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5}
memo_reverse = {0:0, 1:2, 2:3, 3:4, 5:5}
def sol(k):
    l = len(memo)
    while True:
        x = memo_reverse.get(k)
        if x or x==0:
            return x
        memo[l] = memo[l-1] + memo[l-2]
        memo_reverse[memo[l]] = l
        l += 1


for _ in range(t):

    n = int(input())
    print(sol(n))