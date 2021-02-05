import sys
input = sys.stdin.readline
t = int(input())
words = [input().strip() for _ in range(t)]

importance = {}
for word in words:
    for idx, w in enumerate(word[::-1]):
        if not importance.get(w,0):
            importance[w] = 10**idx
        else:
            importance[w] += 10**idx

tmp = sorted(list(importance.items()), key=lambda x: x[1],reverse=True)
alpha_to_idx = {a:9-idx for idx, (a,b) in enumerate(tmp)}

score = 0
for word in words:
    for idx, w in enumerate(word[::-1]):
        score += alpha_to_idx[w]*10**(idx)

print(score)