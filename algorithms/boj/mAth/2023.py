import sys
n = int(sys.stdin.readline())

def isprime(k):
    if k==1:
        return False
    i = 2
    while i*i<=k:
        if k%i==0:
            return False
        i += 1
    return True


def sol(n):
    candi = {1:[2, 3, 5, 7]}
    if n==1:
        return candi[1]
    i = 1
    while True:
        lst = candi.get(n)
        if lst:
            return lst
        candi[i+1] = []
        for p in candi[i]:
            for j in range(1,10,2):
                if isprime(int(str(p) + str(j))):
                    candi[i+1].append(int(str(p) + str(j)))
        i+=1

result = sol(n)
for i in result:
    print(i)