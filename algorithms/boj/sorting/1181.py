import sys

input = sys.stdin.readline

n = int(input())

st = list(set([input().strip()  for _ in range(n)]))
st.sort()
st.sort(key=lambda x: len(x))
for s in st:
    print(s)