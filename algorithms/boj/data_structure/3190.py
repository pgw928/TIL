import sys
from collections import deque

#----------- 입력 -----------
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [ tuple(map(int, input().split())) for _ in range(K)]
l = int(input())

rotate = []
for _ in range(l):
    X, C = tuple(input().strip().split())
    rotate.append([int(X), C])
#----------------------------

#---------- 기본세팅 ----------
check = [ [0]*(N+1) for _ in range(N+1)]
for y,x in apples:
    check[y][x] = 1     # 사과 자리 체크

dq = deque()  # 뱀
dq.append((1,1))

dx, dy = 1, 0 # 나아갈 방향
t = 0 # 시간
k = 0 # rotate index
#-----------------------------


while True:

    # 이동방향 결정
    if (k < l) and (rotate[k][0] == t):
        if rotate[k][1] =='D':
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        k += 1
    print('dx:',dx,'dy:', dy)

    t += 1 # 시간 경과

    # 다음 위치 계산
    yy, xx = (dy + dq[-1][0], dx + dq[-1][1])

    # 밖으로 나가거나 몸이랑 부딪히면면 게임끝
    if xx>N or yy>N or xx<1 or yy<1 or (yy, xx) in dq:
        print(t)
        break
    dq.append((yy, xx)) # 머리 움직임


    # 꼬리 이동
    if check[yy][xx] == 0: # 사과 없으면
        dq.popleft()
    else:
        check[yy][xx] = 1  # 사과 먹고 없앰