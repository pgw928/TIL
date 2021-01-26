import sys

input = sys.stdin.readline

n = int(input())
A = map(int, input().split())


def isprime(a):

    if a == 1:
        return False

    i = 2
    while i*i <= a:
        if a%i == 0:
            return False
        i += 1
    return True

score = 0
for i in A:
    if isprime(i):
        score += 1
print(score)