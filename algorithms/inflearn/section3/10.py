import sys
sys.stdin = open('section3/input.txt', 'rt')
graph = [list(map(int, input().split())) for _ in range(9)]

def check():
    
    for i in range(9):
        cnt1 = {k:0 for k in range(1, 10)}
        cnt2 = {k:0 for k in range(1, 10)}
        for j in range(9):
            if cnt1[graph[i][j]]==0:
                cnt1[graph[i][j]] += 1
            else:
                return 'NO'
            if cnt2[graph[j][i]]==0:
                cnt2[graph[j][i]] += 1
            else:
                return 'NO'
    for i in range(3):
        for j in range(3):
            cnt1 = {k:0 for k in range(1, 10)}
            for k in range(3):
                for s in range(3):
                    if cnt1[graph[3*i+k][3*j+s]]==0:
                        cnt1[graph[3*i+k][3*j+s]] += 1
                    else:
                        return 'NO'
    return 'YES'
print(check())
