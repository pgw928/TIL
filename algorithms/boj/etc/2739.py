import sys

n = int(sys.stdin.readline())


def outer(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)[0]} * {func(*args, **kwargs)[1]} = {func(*args, **kwargs)[0]*func(*args, **kwargs)[1]}'
    return wrapper

@outer
def inner(n, i):
    return (n, i)

[print(inner(n, i)) for i in range(1,10)]