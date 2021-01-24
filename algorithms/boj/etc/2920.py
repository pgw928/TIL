A = list(map(int, input().split()))

if A == list(range(1,9)):
    print('ascending')
elif A == list(range(8,0,-1)):
    print('descending')
else:
    print('mixed')

print(list(range(8,0,-1)))