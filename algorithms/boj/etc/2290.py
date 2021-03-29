import sys; input = sys.stdin.readline
s, n = map(int, input().split())
n = str(n)
one = []
one.append([' ']*(s+2))
for _ in range(s):
    one.append([' ']*(s+1) + ['|'] )
one.append([' ']*(s+2))
for _ in range(s):
    one.append([' ']*(s+1) + ['|'] )
one.append([' ']*(s+2))

two = []
two.append([' ']+['-']*s+[' '])
for _ in range(s):
    two.append([' ']*(s+1) + ['|'] )
two.append([' ']+['-']*s+[' '])
for _ in range(s):
    two.append( ['|']+[' ']*(s+1))
two.append([' ']+['-']*s+[' '])


three = []
three.append([' ']+['-']*s+[' '])
for _ in range(s):
    three.append([' ']*(s+1) + ['|'] )
three.append([' ']+['-']*s+[' '])
for _ in range(s):
    three.append([' ']*(s+1) + ['|'] )
three.append([' ']+['-']*s+[' '])

four = []
four.append([' ']*(s+2))
for _ in range(s):
    four.append(['|']+[' ']*s + ['|'] )
four.append([' ']+['-']*s+[' '])
for _ in range(s):
    four.append([' ']*(s+1) + ['|'] )
four.append([' ']*(s+2))

five = []
five.append([' ']+['-']*s+[' '])
for _ in range(s):
    five.append(['|']+[' ']*(s+1))
five.append([' ']+['-']*s+[' '])
for _ in range(s):
    five.append([' ']*(s+1) + ['|'] )
five.append([' ']+['-']*s+[' '])

six = []
six.append([' ']+['-']*s+[' '])
for _ in range(s):
    six.append(['|']+[' ']*(s+1))
six.append([' ']+['-']*s+[' '])
for _ in range(s):
    six.append(['|']+[' ']*s + ['|'] )
six.append([' ']+['-']*s+[' '])

seven = []
seven.append([' ']+['-']*s+[' '])
for _ in range(s):
    seven.append([' ']*(s+1) + ['|'] )
seven.append([' ']*(s+2))
for _ in range(s):
    seven.append([' ']*(s+1) + ['|'] )
seven.append([' ']*(s+2))

eight = []
eight.append([' ']+['-']*s+[' '])
for _ in range(s):
    eight.append(['|']+[' ']*s + ['|'] )
eight.append([' ']+['-']*s+[' '])
for _ in range(s):
    eight.append(['|']+[' ']*s + ['|'] )
eight.append([' '] + ['-'] * s + [' '])

nine = []
nine.append([' ']+['-']*s+[' '])
for _ in range(s):
    nine.append(['|']+[' ']*s + ['|'] )
nine.append([' ']+['-']*s+[' '])
for _ in range(s):
    nine.append([' ']*(s+1) + ['|'] )
nine.append([' '] + ['-'] * s + [' '])

zero = []
zero.append([' ']+['-']*s+[' '])
for _ in range(s):
    zero.append(['|']+[' ']*s + ['|'] )
zero.append([' ']*(s+2))
for _ in range(s):
    zero.append(['|']+[' ']*s + ['|'] )
zero.append([' ']+['-']*s+[' '])

dic = {'0':zero, '1':one,'2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine}
result = [[] for _ in range(2*s+3)]

for idx, k in enumerate(n):
    tmp = dic[k]
    if idx==0:
        for i in range(2*s+3):
            result[i].extend(tmp[i])
    else:
        for i in range(2*s+3):
            result[i].extend([' ']+tmp[i])

for r in result:
    print(''.join(r))