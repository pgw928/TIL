import sys; input = sys.stdin.readline
r, c, m = map(int, input().split())

# 상어의 위치: 2 , 속력 : 1 이동방향: 1, 크기 : 1
# 위 방향 : 1, 아래 방향 : 2, 오른쪽 : 3, 왼쪽 : 4
shark = dict()
for _ in range(m):
    tmp = tuple(map(int, input().split()))
    shark[tmp[:2]] = tmp[2:] # 속도 , 이동방향, 크기0

print(shark)

dd = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)}


def move(b,a, v, d, s):

    count = v
    if d==1:
        # b를 바꿔야함
        while True:
            if count==0:
                return (b, a, v, d, s)
            elif b-count > 1:
                b -= count
                return (b, a, v, d, s)
            elif b-count == 1:
                b = 1
                return (b, a, v, 2, s)
            elif b-count < 1:
                b = 1


    elif d==2:
        pass
        # b를 바꿔야함
    elif d==3:
        pass
        # a를 바꿔야함
    elif d==4:
        pass
        # a를 바꿔야함
i = 1
score = 0
while i <= c:
    for j in range(1, r+1):
        if (j, i) in shark:
            score += shark[(j, i)][2]
            del shark[(j, i)]
    i += 1
    for (b, a) in shark:
        v, d, s = shark[(b, a)]


print(score)