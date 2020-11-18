# append vs extend

> Python의 `append`와 `extend`의 차이를 예제를 통해 알아본다.

* `list.append(x)`의 경우 `x`자체를 list를 추가해준다.
* `list.extend(x)`의 경우 `x`안에  있는 iterable의 모든 항목을 추가해준다.



## 예제1

```python
x = ['a', 'b', 'c']
y = ['d']
z = ['d']

y.append(x)
print(y)
# ['d', ['a', 'b', 'c']]
z.extend(x)
print(z)
# ['d', 'a', 'b', 'c']
```



## 예제2

```python
x = [['a', 'b'], ['c', 'd'], ['e', 'f']]

y = [['x', 'y']]
z = [['x', 'y']]

y.append(x)
print(y)
# [['x', 'y'], [['a', 'b'], ['c', 'd'], ['e', 'f']]]
z.extend(x)
print(z)
# [['x', 'y'], ['a', 'b'], ['c', 'd'], ['e', 'f']]
```