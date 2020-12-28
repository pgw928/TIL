import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())
#
# print(E, S, M)
# E : 1 ~ 15
# S : 1 ~ 28
# M : 1 ~ 19
while True:
    if (E==S) and (S==M) and (E==M):
        break
    if E<=S and E<=M :
        E += 15
    elif S<=E and S<=M:
        S += 28
    elif M<=S and M<=E:
        M += 19
    print(f'E : {E}, S : {S}, M : {M}')
print(E)

