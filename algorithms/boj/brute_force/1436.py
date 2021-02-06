n = int(input())
six = '666'
lst = list()
count = 0
for i in range(1,10000*1000):
    if six in str(i):
        result = i
        count+=1
    if count == n:
        break

print(result)

