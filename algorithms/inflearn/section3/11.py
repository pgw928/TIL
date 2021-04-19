import sys
sys.stdin = open('section3/input.txt', 'rt')
graph = [input().rstrip().split() for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        tmp1 = graph[i][j:j+5]
        tmp2 = graph[j][i]+graph[j+1][i]+graph[j+2][i]+graph[j+3][i]+graph[j+4][i]
        if tmp1 == tmp1[::-1]:
            cnt += 1
        if tmp2 == tmp2[::-1]:
            cnt += 1
print(cnt)