n = int(input())

s_n = lambda x:  3*(x-1)*x + 1


def sol():
    if n == 1:
        return 1
    i = 2
    while True:

        if s_n(i-1) < n <= s_n(i):
            return i
        i += 1

print(sol())