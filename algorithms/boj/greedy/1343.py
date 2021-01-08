import sys

s = sys.stdin.readline().strip()
A = 'AAAA'
B = 'BB'

statement = s.split('.')
result = []
def solution(statement):
    for word in statement:
        if word == '':
            result.append('')
            continue

        else:
            l = len(word)
            if l%2 == 1:
                return -1
            if l%4 == 0:
                result.append(A*(l//4))
            elif l%4 == 2:
                result.append(A*(l//4)+B)
    return '.'.join(result)

print(solution(statement))
