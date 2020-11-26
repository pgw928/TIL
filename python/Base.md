# Base

> Python에서의 2진법(Binary system), 8진법(Octal), 16진법(Hexadecimal)에 대해서 알아본다. 

2진법~16진법은 10진법과 다르게 앞에 다음과 같은 문자가 붙는다.

* 2진법 : 0b
* 8진법 : 0o
* 16진법 : 0x, 0X

```PYTHON
print(42==0b101010)
# True
print(42 == 0o52)
# True
print(42 == 0x2a)
# True
```





## n진법 자체함수 이용

> 제일 간단하고 쉬운 방법이다. 대신 명령어 기억하면 된다.

* 2진수 : `bin`
* 8진수 : `oct`
* 16진수 : `hex`

```python
print(bin(42))
# 0b101010
print(type(bin(42)))
# <class 'str'>

print(oct(42))
# 0o52
print(hex(42))
# 0x2a
```





## int 함수를 활용한 변환

>  `int(x,y)`를 사용해 10진수로 변환해 준다.  `x` 인자는 문자열로 n진법 수를 입력해주고 `y`인자로는 이것이 몇진법인지 입력해준다.

```python
print(int('0b10', 2))
# 2
print(int('0b10', 2))
# 42
print(int('0o52', 8))
# 42
```



## format 함수를 활용한 n진법으로의 변환

> format 함수를 이용해 진법 표현을  나타낼지 선택이 가능하다.

* 진법 표현 없이

```python
print(format(42,'b'))
# 101010
print(format(42,'x'))
# 2a
print(format(42,'X'))
# 2A
print(format(42,'o'))
# 52
print(format(42,'d'))
#42
```

* 진법 표현 포함

```python
print(format(42,'#b'))
# 0b101010
print(format(42,'#x'))
# 0x2a
print(format(42,'#X'))
# 0X2A
print(format(42,'#o'))
# 0o52
print(format(42,'#d'))
# 42
```



