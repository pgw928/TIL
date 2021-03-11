import sys; input = sys.stdin.readline
n = int(input())
distance = tuple(map(int, input().split()))
cities = tuple(map(int, input().split()))


m = cities[0]
r = 0
for c, d in zip(cities[:-1], distance):
    if c < m:
        m = c
    r+=d*m
print(r)