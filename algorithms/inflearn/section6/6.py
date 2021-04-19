import sys
sys.stdin = open('section6/input.txt', 'rt')
n, m = map(int, input().split())
cnt = 0
# def dfs(tp):
#     global cnt
#     if len(tp)==m:
#         print(' '.join(list(map(str, tp))))
#         cnt += 1
#         return
#     for i in range(1, n+1):
#         dfs(tp+(i,))
# for i in range(1, n+1):
#     dfs((i,))
# print(cnt)


def dfs(x):
    global cnt
    if x==m:
        print(' '.join(map(str, visited)))
        cnt += 1
        return
    for i in range(1, n+1):
        visited[x] = i
        dfs(x+1)
        visited[x] = 0

visited = [0]*(m)
dfs(0)
print(cnt)