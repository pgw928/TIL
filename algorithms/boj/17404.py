import sys; input = sys.stdin.readline
n = int(input())
rgb = [tuple(map(int, input().split())) for _ in range(n)]

dp1 = [[[0, 0] for _ in range(3)] for _ in range(n)]

for i in range(2, n):
    if dp1[i-1][1][0] <= dp1[i-1][2][0]:
        dp1[i][0][0] = rgb[i-1][0]
        dp1[i][0][1] = 0

    dp1[i][0][0] = rgb[i-1][0] + min(dp1[i-1][1][0], dp1[i-1][2][0])
    dp1[i][1][0] = rgb[i-1][1] + min(dp1[i-1][0][0], dp1[i-1][2][0])
    dp1[i][2][0] = rgb[i-1][2] + min(dp1[i-1][1][0], dp1[i-1][0][0])

# result = [rgb[0][0]+rgb[-1][2]+dp1[-1][1], rgb[0][0]+rgb[-1][2]+dp1[-1][1],
#           rgb[0][0]+rgb[-1][1]+dp1[-1][2], rgb[0][1]+rgb[-1][0]+dp1[-1][2],
#           rgb[0][2]+rgb[-1][1]+dp1[-1][0], rgb[0][1]+rgb[-1][2]+dp1[-1][0]]
for d in dp1:
    print(d)

# print(min(result))
