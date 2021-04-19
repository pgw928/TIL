import sys
sys.stdin = open('section2/input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))
m = int(sum(arr)/n + 0.5)
res = sorted([(abs(m-k),k,idx)  for idx, k in enumerate(arr,1)], key=lambda x: (x[0], -x[1], x[2]))[0][2]

print(m ,res)
