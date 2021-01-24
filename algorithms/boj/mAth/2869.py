import sys

a, b, v = map(int, sys.stdin.readline().split())

if (v-a)%(a-b)==0:
    print((v-a)//(a-b)+1)

else:
    print((v-a)//(a-b)+2)
