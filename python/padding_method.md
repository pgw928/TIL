# padding method

> 기본 python에 있는 padding method `rjust`, `ljust`, `zfill`에 대해서 알아본다.



## rjust

> 오른쪽 정렬을 기준으로 왼쪽에 원하는 문자로 padding 해준다. 입력인자로 원하는 문자열 길이 양의 정수와 한 글자의 문자가 들어간다.

* 예시

```python
a = '77'.rjust(5,'가')
print(a)
# 가가가77

b = 'def'.rjust(5, '0')
print(b)
# 00def

c = 'qwe'.rjust(3, '0')
print(c)
# qwe
```





## ljust

> `rjust`와 기능은 갖고 왼쪽정렬을 기준으로 오른쪽에 원하는 문자를 padding 해준다. 따라서 원하는 길이의 문자열을 만들어준다.

* 예시

```python
a = '77'.ljust(5,'가')
print(a)
# 77가가가

b = 'def'.ljust(10, '0')
print(b)
# def0000000
```



## zfill

> `rjust`와 비슷한 기능으로 문자열 기준 왼쪽에 padding을 해준다. (기존 문자열 오른쪽 정렬) 하지만 문자열을 오로지 `'0'`으로만 padding 해주고 입력인자로 원하는 문자열의 길이만 입력해준다.

* 예시

```python
a = '문자열'.zfill(3)
print(a)
# 문자열

b = 'abc'.zfill(5)
print(b)
# 00abc

c = '123'.zfill(10)
print(c)
# 0000000123
```





#### ※ 세가지 method 모두 원래의 문자열 보다 길이가 작으면 아무일도 일어나지 않는다.

