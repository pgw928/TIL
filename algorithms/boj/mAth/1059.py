import sys

input = sys.stdin.readline

L = int(input())

S = sorted(list(map(int, input().split())))

n = int(input())

def solution(n,S):
    bound = [0, 0]
    for i, u in enumerate(S):
        if i==0:
            if n < u:
                bound[1] = u
                break
            else:
                continue
        if S[i-1]<n<u:
            bound[0], bound[1] = S[i - 1], u
            break

    u, v = (bound[0], bound[1])
    if u==v:
        return 0
    else:
        return (n-u-1)*(v-n-1)+(v-n-1)+(n-u-1)

print(solution(n,S))



