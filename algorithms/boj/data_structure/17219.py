import sys; input = sys.stdin.readline
n, m = map(int, input().split())

site_to_pass = {}
for i in range(1, n+1):
    site, passw = input().strip().split()
    site_to_pass[site] = passw

for _ in range(m):
    q = input().strip()
    print(site_to_pass[q])
