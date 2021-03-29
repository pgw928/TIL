import sys; input = sys.stdin.readline
n, k = map(int, input().split())
result = []
def dfs(s):
    if eval(s)==n:
        result.append(s)
        return
    if eval(s+'+1') <= n:
        dfs(s+'+1')
    if eval(s+'+2') <= n:
        dfs(s+'+2')
    if eval(s+'+3') <= n:
        dfs(s+'+3')
dfs('1')
dfs('2')
dfs('3')
if len(result) < k:
    print(-1)
else:
    print(result[k-1])