import sys
n = int(sys.stdin.readline())

def isprime(k):

    if k==0 or k==1:
        return False
    i = 2
    while i*i<=k:
        if k%i==0:
            return False
        i+=1
    return True

count = 0
i = 2
while True:
    if isprime(i):
        count += 1
    if count==n:
        print(i)
        break
    i+= 1