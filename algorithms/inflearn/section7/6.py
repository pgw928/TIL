import sys
sys.stdin = open('section7/input.txt', 'rt')
n = input().rstrip()
l = len(n)
res = []
def dfs(x, s):
    if x==l:
        res.append(s)
        return
    t_n = int(n[x:x+2])
    if x+2 <= l and 9<t_n<=26:
        dfs(x+2, s + chr(t_n+64) )
    t_n = int(n[x]) 
    if t_n > 0:
        dfs(x+1, s + chr(t_n+64) )

dfs(0, '')
res.sort()
for r in res:
    print(r)
print(len(res))