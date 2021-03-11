import sys; input = sys.stdin.readline
n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

i, j = 1, house[-1] - house[0]

while i < j-1:
    ''' i : 최소거리
        j : 최대거리
        m : 중간값 '''
    m = (i+j)//2
    count, idx = 1, 0
    for k in range(1, n):
        if house[k]- house[idx] >= m:
            print(house[idx],'기준',house[k],'에 설치')
            count += 1
            idx = k
    print(count)
    if count >= c: # 공유기를 더 많이 설치했을 때 => 최대거리가 너무 짧다
        i = m
    elif count < c: # 공유기를 더 적게 설치했을 때 => 최대거리가 너무 크다.
        j = m
print(i)