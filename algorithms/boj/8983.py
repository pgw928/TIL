import sys; input = sys.stdin.readline
m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
animal = dict()
for _ in range(n):
    x, y = map(int, input().split())
    animal[(x, y)] = False

for a in sade:
    for x, y in animal:
        if not animal[(x, y)] and abs(x-a)+y<=l:
            animal[(x, y)] = True
print(sum(animal.values()))
