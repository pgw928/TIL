import sys
n = int(input())

def counter(n, div):
    count = 0
    while True:
        count += n//div
        n //=div
        if n == 0:
            return count

print(min(counter(n, 2), counter(n, 5)))
