## closure

> **위키피디아** : 일급 객체 함수(first-class functions)의 개념을 이용해 스코프(scope)에 묶인 변수를 바인딩 하기 위한 일종의 기술이다.

### 예제

```python
def my_outer_func():
    a, b = 3, 5
    def my_inner_func():
        print(a, b)
    return my_inner_func
```

* 예를 통해 쉽게 생각하면, `my_func = my_outer_func()`와 같이 `my_inner_func`를 호출했을 때, `a, b` 변수가 어딘가에 저장되는 기술이 **closure**이다.



### 살펴보기

```python
my_func = my_outer_func()
```

* 위와 같이 정의했을 때 `my_inner_func`를 받아오는 것을 알 수 있다.

```python
print(f'my_func의 type : {type(my_func)}')
# my_func의 type : <class 'function'>

print(f'my_func의 closure의 type : {type(my_func.__closure__)}')
# my_func의 closure의 type : <class 'tuple'>

print(f'my_func의 closure의 length :  {len(my_func.__closure__)}')
# my_func의 closure의 length :  2

print(f'첫 번째 성분 : {my_func.__closure__[0].cell_contents}')
# 첫 번째 성분 : 3

print(f'두 번째 성분 : {my_func.__closure__[1].cell_contents}')
# 두 번째 성분 : 5
```

* my_func의 closure는 tuple형태로 참조하는 변수들이 저장되는 것을 알수있다.

