import sys

n = int(sys.stdin.readline())
s = '*'
def recursion(n):
    global s
    if n == 1:
        return s
    # padding
    lst = s.split('\n')
    l = len(lst[0])

    tmp = '*'*(l+4) +'\n' + '*'+(l+2)*' '+ '*'
    for star in lst:
        tmp += '\n' + '* ' + star + ' *'

    tmp += '\n'+ '*'+(l+2)*' '+ '*' +'\n' + '*'*(l+4)

    s =  tmp
    recursion(n-1)
    return s

print(recursion(n))