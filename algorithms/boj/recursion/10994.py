import sys

n = int(sys.stdin.readline())
s = '*****'+'\n*    '+'\n* ***'+'\n* * *'+'\n* * *'+'\n*   *'+'\n*****'

def recursion(n):
    global s
    if n == 1:
        return '*'

    if n == 2:
        return s

    lst = s.split('\n')
    l = len(lst[0])

    tmp = '*'*(l+4) +'\n' + '*'+(l+3)*' '
    tmp += '\n'+'* '+lst[0]+'**'
    for star in lst[1:]:
        tmp += '\n' + '* ' + star + ' *'

    tmp += '\n'+ '*'+(l+2)*' '+ '*' +'\n' + '*'*(l+4)

    s =  tmp
    recursion(n-1)
    return s

result = recursion(n).split('\n')
for r in result:
    print(r.strip())