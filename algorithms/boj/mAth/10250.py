import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H ,W, N = map(int, input().split())
    q, r = divmod(N, H)
    if r==0:
        front = str(H)
    else:
        front = str(r)

    if  (r != 0) and (q < 9):
        print(front + '0' + str(q+1) )
    elif (r == 0) and (q < 10):
        print(front + '0' + str(q))
    elif (r != 0) and (q >= 9):
        print(front + str(q+1) )
    elif (r == 0) and (q >= 10):
        print(front + str(q))