import sys
sys.setrecursionlimit(3**14)
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_fun(x1, y1, x2, y2):
    tmp = graph[y1][x1]
    for i in range(x1,x2):
        for j in range(y1,y2):
            if tmp != graph[j][i]:
                return True
    return False

result ={0:0, -1:0, 1:0}
def divide_conqure(x1, y1, x2, y2):
    if x1==x2:
        result[graph[y1][x1]]+=1
    elif check_fun(x1, y1, x2, y2):
        l = (x2-x1)//3
        for i in range(3):
            for j in range(3):
                n_x1, n_x2 = x1 + l*j, x1 + l*(j+1)
                n_y1, n_y2 = y1 + l*i, y1 + l*(i+1)
                divide_conqure(n_x1, n_y1, n_x2, n_y2)
    else:
        result[graph[y1][x1]]+=1

divide_conqure(0, 0, n, n)
print(result[-1])
print(result[0])
print(result[1])