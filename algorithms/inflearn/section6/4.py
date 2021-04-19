import sys
sys.stdin = open('section6/input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))
check = {a:0 for a in arr}
res = 'NO'
def dfs(node):
    global res
    if node == n-1:
        left = sum([a for a in check if check[a]==1])
        right = sum([a for a in check if check[a]==0])
        if left==right:         
            print('YES')
            sys.exit(0)
    if node+1 < n:
        check[arr[node+1]] = 1
        dfs(node+1)
        check[arr[node+1]] = 0
        dfs(node+1)

dfs(0)
print('NO')