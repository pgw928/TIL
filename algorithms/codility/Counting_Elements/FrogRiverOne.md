# FrogRiverOne

> 처음 문제가 이해가 안되서 계속 읽어보고 구글링도 많이 해봤는데  핵심은 `that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves` 이 문장으로, 이것을 놓치면 문제를 파악할 수 없었다.
>
> 문제 풀이는 O(N**2) 이 아닌 어떻게 O(N) 으로 해결하냐이다.



## 문제

```
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
```



## 최종 풀이

> `for`문 안에서 한번에 여러 작업을 하려하지 않고 나눠서 작업 하려고 고민했다. 

```python
def solution(X, A):
    
    check = [-1]*(X+1)
    
    for i in range(len(A)):
        if check[A[i]] == -1:
            check[A[i]] = i
    
    if -1 in check[1:]:
        return -1
    else:
        return max(check[1:])
```

: O(N)





## 다른 사람 풀이

> `check`와 `check_sum` 을 한번에 이용한다는게 point

```python
def solution(X, A):
    check = [0] * (X+1)
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]] == 0:
            check[A[i]] = 1
            check_sum += 1
        if check_sum == X:
            return i
    return -1
```

: O(N)

