# python method, function 정리

> 알고리즘을 하면서 배우는 method, function을 정리한다.



* 숫자, 문자열인지 확인

```python
print('a'.isalpha())
# True

print('한글'.isalpha())
# True

print(3.isdigit())
# True
```



* `lambda`함수를 활용한 정렬

```python
points =[(2, 2), (0, 3), (1, 1), (4, 1)]
points.sort(key=lambda x: x[0])
print(points)

# [(0, 3), (1, 1), (2, 2), (4, 1)]
```



* inf 값 활용

```python
import math
a = math.inf
print(a)
# inf
print(-math.inf)
# -inf
```

