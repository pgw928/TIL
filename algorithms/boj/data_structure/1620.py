import sys; input = sys.stdin.readline
n, m = map(int, input().split())

idx_to_name = {}
name_to_idx = {}
for i in range(1, n+1):
    name = input().strip()
    idx_to_name[i] = name
    name_to_idx[name] = i

for _ in range(m):
    q = input().strip()
    if q[0].isnumeric():
        print(idx_to_name[int(q)])
    else:
        print(name_to_idx[q])