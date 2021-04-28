import sys
sys.stdin = open('section7/input.txt', 'rt')
n, m = map(int ,input().split())
point, time = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    point.append(a)
    time.append(b)
total = sum(point)

res = 0
def dfs(x, t, val):
    global res
    if val > res:
        res = val
        
    for y in range(x+1, n+1):
        if time[y] + t <= m:
            dfs(y, t+time[y], val+point[y])



dfs(0, 0, 0)
print(res)