import sys

input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    edges.append((a, b, c))
edges.sort(key=lambda x : (x[2], x[0]))

graph = {i:[] for i in range(1,v+1)}
for a, b, c in edges:
    graph[a].append(b)
    graph[b].append(a)

print(graph)
print(edges)



def is_safe(x, y):
    if not mst:
        return True
    if (x in vert) and (y in vert):
        tmp = x
        check = set()

        while True:
            res = check.copy()
            for v1, v2 in mst:
                if (v1, v2) in check:
                    continue
                elif (v1, v2) not in check:
                    check.add((v1, v2))
                    if tmp==v1:
                        tmp = v2
                    elif tmp==v2:
                        tmp = v1
                    if tmp == y:
                        return False
            if res==check:
                return True
    return True

#
mst = set()
vert = set()
result = 0
for i in range(e):
    x, y, w = edges[i]
    if is_safe(x, y):
        vert.add(x)
        vert.add(y)
        mst.add((x, y))
        print(mst)
        result += w
print(mst)
print(result)