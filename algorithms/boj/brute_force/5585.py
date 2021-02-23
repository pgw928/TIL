import sys
pay = 1000 - int(sys.stdin.readline())

money = [500, 100, 50, 10, 5, 1]

count = 0
i = 0
while pay!=0:
    q, r = divmod(pay, money[i])
    if q > 0:
        count += q
        pay = r
    else:
        i += 1
print(count)


