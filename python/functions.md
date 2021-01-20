# 파이썬 다양한 함수

> 내가 모르는 python 함수에 초점을 맞쳐 정리한다.



## 1. ord

> 문자의 아스키 코드 값을 돌려주는 함수이다.

```python
print(ord('a')) # 97
print(ord('A')) # 65
print(ord('z')) # 122
```





## 2. chr 

> `ord`의 반대되는 함수로 아스키(ASCII) 코드 값을 입력받아 해당하는 문자를 출력한다.

```PYTHON
for i in range(ord('A'), ord('Z')+1):
    print(chr(i) , end='')
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
```



#### 3. round

> 반올림 함수이다.

```python
print(round(123.5567))		# 124
print(round(123.5567, 3))	# 123.557
print(round(123.5567, -1))  # 120.0
```

