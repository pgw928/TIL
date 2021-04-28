import sys
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
profit, days = [], []
for i in range(n):
    a, b = map(int, input().split())
    days.append(a)
    profit.append(b)
res = 0
def dfs(x, p):
    global res
    if x>n:
        return
    
    if x==n:
        if p>res:
            res = p
        return

    dfs(x+days[x], p + profit[x] )
    dfs(x+1, p)

dfs(0, 0)
print(res)