import sys; input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = int(input()), int(input())
l = len(str(n))
if m > 0:
    arr = set(map(int, input().split()))
else:
    arr = set()
remote = {i for i in range(10)}

diff = abs(100-n)
def click_num(s, depth):
    global diff, k
    if l-1>0 and l-1==depth:
        if abs(int(s)-n) < diff:
            diff, k = abs(int(s)-n), int(s)
        elif abs(int(s)-n)==diff:
            if len(str(int(s))) < len(str(k)):
                diff, k = abs(int(s) - n), int(s)


    elif depth==l:
        if abs(int(s)-n) < diff:
            diff, k = abs(int(s)-n), int(s)
        elif abs(int(s) - n) == diff:
            if len(str(int(s))) < len(str(k)):
                diff, k = abs(int(s) - n), int(s)

    elif depth==l+1:
        if abs(int(s)-n) < diff:
            diff, k = abs(int(s)-n), int(s)
        elif abs(int(s)-n)==diff:
            if len(str(int(s))) < len(str(k)):
                diff, k = abs(int(s) - n), int(s)

        return

    for a in remote-arr:
        click_num(s+str(a), depth+1)



if len(arr)== 10:
    print(abs(100 - n))
else:
    click_num('', 0)
    print(min(abs(100-n), abs(n-k)+len(str(k))))
