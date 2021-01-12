# TapeEquilibrium

> 생각보다 어렵지 않게 쉽게 해결했다.



## 문제

```
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
```



## 최종 풀이

> default 값의 `front`와 `back` 값을 주고 `while`문을 사용해 하나씩만 읽어서 `min`함수를 사용해  최솟값을 비교해 값을 찾았다.

```python
def solution(A):
    
    front = A[0]
    back = sum(A[1:])
    diff = abs(front-back)

    i = 1
    n = len(A)

    while i < n-1:
        front += A[i]
        back -= A[i]
        tmp = abs(front-back)
        diff = min(tmp, diff)
        i += 1
    return diff
```

: O(N) 

