# Numpy iterator

> `array`의 원소를 하나씩 출력할 때 주로 `forloop`을 사용하게 된다. 그러나 `array`의 차원이 늘어날수록 `forloop`의 개수가 많아져야 하고 그만큼 속도가 느려질 수 있다. 그러나 `Numpy`에서는 `iterator` 라는것을 제공해준다. `nditer` 라는 keyword를 이용하며 `index`, `iternext`, `finished` 속성을 알아야 한다.

## 1차원 array

> 다음의 예제를 통해 알아본다.

```python
arr = np.array(['a', 'b', 'c', 'd', 'e'])
print(arr)  # ['a' 'b' 'c' 'd' 'e']
```

* 일반적으로 다음과 같은 방법으로 출력할 수 있다.

```python
for tmp in arr:
    print(tmp, end=' ')
# a b c d e 
```

* `nditer`를 만들어 우선 무엇인지 확인해본다.

```python
it = np.nditer(arr, flag=['c_index']) # c언어에서 쓰던 index
# 무엇인지 알아보기 위해 forloop를 돌려본다.
for i in it:
    print(i)
# a
# b
# c
# d
# e
```

* while 문을 사용해 추출해 본다. `finished`, `index`, `iternext` keyword를 사용한다.

```python
while not it.finished: # iterator가 지정하는곳이 끝인지 True, False로 나타낸다.
    idx = it.index  # iterator가 '현재' 가리키는 곳의 index를 가져온다.
    print(arr[idx], end=' ')
    it.iternext()  # True/False 값으로 항상 True값이다가 마지막 index시 더이상 다음으로 못가므로 False값을 갖는다.
```



```python
for row in range(arr.shape[0]):
	for col in range(arr.shape[1]):
        print(arr[row,col], end=' ')
# 1 2 3 4 5 6 
```

* `nditer`를 이용한 방법으로 `while`문 하나로 출력 가능하다.

```python
it = np.nditer(arr, flag=['c_index']) # c언어에서 쓰던 index
while not it.finished:
```





