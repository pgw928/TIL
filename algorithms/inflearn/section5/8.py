import sys
sys.stdin = open('section5/input.txt', 'rt')
n = int(input())
memo = {}
for _ in range(n):
    s = input().rstrip()
    memo[s] = memo.get(s, 0) + 1
for _ in range(n-1):
    s = input().rstrip()
    memo[s] = memo.get(s) - 1 
print(memo)
for s in memo:
    if memo[s] == 1:
        print(s)
        break
