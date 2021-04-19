import sys
sys.stdin = open('section6/input.txt', 'rt')

res = float('inf')
def dfs(s, cnt):
    global res
    if s > m or cnt > res:
        return
    if s==m:
        if cnt <res:
            res = cnt
        return
    for a in arr:
        if a+s<=m:
            dfs(a+s, cnt+1)
if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().split()))[::-1]
    m = int(input())
    dfs(0,0)
    print(res)
    
    