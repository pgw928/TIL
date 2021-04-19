import sys
sys.stdin = open('section2/input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))

def isPrime(x):
    if x==1:
        return False    
    i = 2
    while i*i<=x:
        if x%i==0:
            return False
        i += 1
    return True

# def reverse(x):
#     return int( str(x)[::-1] )

def reverse(x):
    ret = 0
    while x>0:
        ret = ret*10 + x%10
        x //= 10        
    return ret


for x in arr:
    x = reverse(x)
    if isPrime(x):
            print(x, end=' ')
