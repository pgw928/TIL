# 문자열 메소드

> 문자열 메소드에 대해서 정리한다.



## 검색 메소드

> 문자열 검색 메소드에 대해 알아본다.

```python
s = 'python programming'
```



| **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| p     | y     | t     | h     | o     | n     |       | p     | r     | o     | g      | r      | a      | m      | m      | i      | n      | g      |

#### 1. find

: find method는 인수로 지정한 문자 또는 부분 문자열을 조사한다.

```python
print(s.find('o')) # 4  : 해당하는 index를 알려준다.
print(s.find('z')) # -1 : 해당하는 문자가 존재하지 않으면 -1을 출력한다.
```



#### 2. index

: index method도 find와 기능은 같지만, 값이 없을 때 예외가 발생한다. 따라서 `find`보다 쓰기 조금 까다롭다.

```python
print(s.index('o')) # 4 : 해당하는 index를 알려준다.
print(s.index('z'))
# Traceback (most recent call last):
#   File "C:/Users/User/Desktop/GIT/TIL/algorithms/boj/tmp.py", line 3, in <module>
#     print(s.index('z'))
# ValueError: substring not found
```



#### 3. rfind

: 오른쪽에서 부터 검색한다는 점을 제외하고 find와 같은 기능을 갖는다.

```python
print(s.rfind('o')) # 9
print(s.rfind('z')) # -1
```



#### 4. rindex

: 오른쪽에서 부터 검색한다는 점을 제외하고 index와 같은 기능을 갖는다.

```python
print(s.rfind('o')) # 9
print(s.rfind('z')) 
# Traceback (most recent call last):
#   File "C:/Users/User/Desktop/GIT/TIL/algorithms/boj/tmp.py", line 3, in <module>
#     print(s.rindex('z'))
# ValueError: substring not found
```



## 조사 메소드

> 문자열 관련 조사 메소드에 대해서 알아본다.



#### 1. startswith

: 특정 문자열로 시작하는지 조사한다. 앞부분의 일부만 비교한다는 점과 `True/False`로 값을 얻는다는 점에서 `find`와 `index`와 다르다.

```python
name = '최익현'

if name.startswith('최'):
    print('실례지만 거 어데~~최씨입니까?')
else:
    print('대구빡이 딱 우리 집안 사람이 아니네..')
    
# 실례지만 거 어데~~최씨입니까?
```



#### 2. endswith

: 끝에서 부터 찾는다는 점을 제외하고 `startswith`와 같은 기능을 지닌다.

```python
file = 'temp.jpg'

if file.endswith('.jpg'):
    print('jpg 파일입니다.')
else:
    print('jpg가 아닙니다.')
    
# jpg 파일입니다.
```



* 추가 조사 method

| 메소드        | 설명                                                   |
| ------------- | ------------------------------------------------------ |
| isalpha()     | 모든 문자가 알파벳인지 조사한다.                       |
| islower()     | 모든 문자가 소문자인지 조사한다.                       |
| isupper()     | 모든 문자가 대문자인지 조사한다.                       |
| isspace()     | 모든 문자가 공백인지 조사한다.                         |
| isalnum()     | 모든 문자가 알파벳 또는 숫자인지 조사한다.             |
| isnumeric()   | 모든 문자가 숫자인지 조사한다.                         |
| isdecimal()   | 모든 문자가 숫자인지 조사한다.                         |
| isdigit()     | 모든 문자가 숫자인지 조사한다.                         |
| isidentifier  | 명칭으로 쓸 수 있는 문자로만 구성되어 있는지 조사한다. |
| isprintable() | 인쇄 가능한 문자로만 구성되어 있는지 조사한다.         |

