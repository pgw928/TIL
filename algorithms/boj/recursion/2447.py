import sys
n = int(sys.stdin.readline())
# ***
# * *
# ***

def rep(n):
    if n==3:
        return ['***', '* *', '***']
    else:
        tmp = rep(n/3)
        l = len(tmp[0])
        result = tmp[:]
        for i in range(len(tmp)):
            result[i] *= 3

        result += [tmp[i]+' '*l+tmp[i] for i in range(l)]
        for i in range(len(tmp)):
            result.append(tmp[i]*3)

        return result

res = rep(n)
print('\n'.join(res))