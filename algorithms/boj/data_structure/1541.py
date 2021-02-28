import sys

eq = sys.stdin.readline().strip()
tmp = []
k = 0
for idx, s in enumerate(eq):
    if not s.isnumeric():
        if k!=idx:
            tmp.append((str(int(eq[k:idx]))))
        tmp.append(s)
        k = idx+1
tmp.append(str(int(eq[k:])))
eq = ''.join(tmp)

count =0
stack = []
for s in eq:
    if s!='-':
        stack.append(s)
    else:
        if count > 0:
            stack.append(')')
            stack.append('-')
            stack.append('(')
        else:
            stack.append('-')
            stack.append('(')
            count +=1
for _ in range(count):
    stack.append(')')

print(eval(''.join(stack)))
