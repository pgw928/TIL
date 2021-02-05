import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = sorted(list(map(int, input().split())))

print(m)

def binary_search(A, m):
    result = 0
    start = 0
    end = A[-1]
    while start <= end:
        # print(start, end)
        mid = (start+end)//2
        s = sum([a-mid for a in A if a-mid>0])
        print(f'sum:{s}, m:{m}')
        if s == m:
            result = mid
            return result
        elif s < m:
            print(f'elif : start:{start}, end:{end}, mid:{mid}')
            end = mid-1
        else:
            print(f'else : start:{start}, end:{end}, mid:{mid}')
            result = max(mid, result)
            start = mid+1
    return result

print(binary_search(A,m))
