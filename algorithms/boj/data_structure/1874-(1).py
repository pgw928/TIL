import sys

input = sys.stdin.readline

n = int(input())
given = [int(input()) for _ in range(n)] # 주어진 수열
def sol():
    result,  stack = ( [], [])
    pointer = 1
    for i in range(n):

        current = given[i]
        for j in range(pointer, current+1): # push
            stack.append(j)
            result.append('+')
            pointer += 1

        result.append('-')
        print(stack)
        if given[i] != stack.pop():
            return 'NO'
    return '\n'.join(result)

print(sol())