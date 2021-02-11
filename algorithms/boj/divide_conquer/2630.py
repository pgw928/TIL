import sys
sys.setrecursionlimit(128*128)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]



def check_fun(g):
    check = set()
    for i in range(len(g)):
        for j in range(len(g)):
            check.add(g[i][j])
            if len(check) > 1:
                return True
    return False


def divide_conqure(g):
    global blue, white
    # if len(g)==1:
    #     if graph[0][0]==0:
    #         white += 1
    #     else:
    #         blue += 1

    if check_fun(g):
        l = len(g)
        g1 = [g[i][:l//2] for i in range(l//2)]
        g2 = [g[i][:l//2] for i in range(l//2,l)]
        g3 = [g[i][l//2:] for i in range(l//2)]
        g4 = [g[i][l//2:] for i in range(l//2,l)]
        divide_conqure(g1)
        divide_conqure(g2)
        divide_conqure(g3)
        divide_conqure(g4)
    else:
        print(g)
        if g[0][0]==0:
            white += 1
            print('white', white)
        else:
            blue += 1
            print('blue', blue)
blue = 0
white = 0

divide_conqure(graph)
print(white)
print(blue)