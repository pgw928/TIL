import sys

n = int(sys.stdin.readline())
cycle = 0
pre = n
new = -1
while n!=new:
    if pre%10==pre:
        pro = pre
        new = (pre) * 10 + pro%10
        pre = new
    else:
        pro = pre//10 + pre%10
        new = (pre%10) * 10 + pro%10
        pre = new
    cycle += 1

print(cycle)