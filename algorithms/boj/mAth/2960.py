import sys

N, K = map(int, sys.stdin.readline().split())

numbers = list(range(N+1))
numbers[1] = 0

i = 2
count = 0
break_point = False
while True:
    for j in range(i,N+1,i):
        if numbers[j]!=0:
            tmp = numbers[j]
            numbers[j] = 0
            count += 1
            if count == K:
                print(tmp)
                break_point = True
                break
    if break_point:
        break
    i+=1


