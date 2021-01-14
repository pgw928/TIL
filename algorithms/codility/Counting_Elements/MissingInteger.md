# MissingInteger

> sorting 하고 중간에 빈부분 찾으면 되는 문제라 쉽게 해결했다.



## 문제

```
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
```



 ## 최종 풀이 

```python
def solution(A):

    A.sort()
    max_num = 0
    for n in A:
        if n == max_num + 1 :
            max_num = n
    return max_num + 1
```

 : O(N) or O(N*log(N))

