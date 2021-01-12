# 두번째 시도 코드

```python
def solution(N, A):
    
    count = [0]*N
    n = len(A)
    M = 0
    for i in range(n):
        if A[i] < N+1:
            count[A[i]-1] += 1
            M = max(M, count[A[i]-1])
        else:
            count = [M]*N
        
    return count
```

**O(N + M)**

: 실패