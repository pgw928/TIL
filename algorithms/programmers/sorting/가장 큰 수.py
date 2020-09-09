ans = ''
numbers = [3, 30, 34, 5, 9, 35, 37, 33, 31,32]
s_numbers = [str(n) for n in numbers]

sort_n  = sorted(s_numbers, key=lambda x : int(x[0]))[::-1]
print(sort_n)
for i in range(9,0,-1):
