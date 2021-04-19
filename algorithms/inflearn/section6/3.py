import sys
sys.stdin = open('section6/input.txt', 'rt')
n = int(input())


# def dfs(tp):
#     global n
#     if tp[-1] > n:
#         return
#     for i in range(tp[-1]+1, n+1):
#         dfs(tp+(i,))
#         print(' '.join(list(map(str, tp+(i,)))))
#     if len(tp)==1:
#         print(tp[0])
# for i in range(1, n+1):
#     dfs((i,))

visited = [0]*(n+1)
def dfs(k):
    if k==n:
        # print(visited)
        print(' '.join(list(map(str, [idx for idx, a  in enumerate(visited) if a==1]))))
        return
    visited[k+1] = 1
    dfs(k+1)
    visited[k+1] = 0
    dfs(k+1)

for i in range(1, n+1):
    visited[i] = 1
    dfs(i)
    visited[i] = 0
    