import sys
sys.stdin = open('section2/input.txt', 'rt')
n = int(input())
nums = [True]*(n+1)
nums[0], nums[1] = False, False 
for i in range(2, n//2+1):
    for j in range(2*i, n+1, i):
        nums[j] = False
print(sum(nums))