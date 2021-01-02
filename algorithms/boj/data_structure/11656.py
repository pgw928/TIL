import sys

input = sys.stdin.readline().strip()

temp = [ input[i:] for i in range(len(input))]

temp.sort()
for t in temp:
    print(t)
