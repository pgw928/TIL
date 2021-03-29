import sys; input = sys.stdin.readline
n = int(input())
express = input().rstrip()
nums ,ops = [], []
for s in express:
    if s.isdecimal():
        nums.append(s)
    else:
        ops.append(s)

check = set()
def dfs(cur=express[0] , i=0):
    if i==len(ops):
        check.add(int(cur))
        return

    dfs(str(eval(cur+ops[i]+nums[i+1])), i+1 )
    if i+1 < len(ops):
        dfs(str(eval(cur+ops[i] + '('+nums[i+1]+ops[i+1]+nums[i+2]+')')), i+2)

dfs()
print(max(check))