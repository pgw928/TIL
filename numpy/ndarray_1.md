# 여러가지 ndarray-(1)

> ndarray를 만드는 여러가지 방법에 대해서 소개한다.





##  ndarray 타입 지정해 생성하기

`numpy`에는 여러가지 **데이터 타입**이 있지만 대표적인 `int32` 와 `float64` 를 사용해 만들자.

**데이터 타입**을 지정할때는 `dtype` 속성에 값을 주면 된다.

```python
import numpy as np
a= [[1,2,3], [4,5,6]]
arrary = np.array(a, dtype=np.int32)
print(array)       # [[1 2 3]
 				   # [4 5 6]]
print(array.dtype) # int32

array = np.array(a,dtype=np.float64)
print(array)       # [[1. 2. 3.]
				   # [4. 5. 6.]]				   
print(array.dtype) # float64

array = np.array(a, dtype=str)
print(array)       # [['1' '2' '3']
				   # ['4' '5' '6']]
print(array.dtype) # <U1
```





## ndarray를 이용해 preallocation 하기

 `numpy`에서는 `array`의 크기를 미리 알고 있을때 `array`를 사전할당 할 수 있다.

#### 1. zeros

* `array`에 `0`값으로 다채우므로써 사전할당 한다.

* 입력값으로 원하는 `array`의 `shape` 값이 들어간다.

* default `dtype`으로 `float64`으로 지정되고 `dtype`은 따로 설정가능하다.

  ```python
  import numpy as np
  arr = np.zeros((2,5)) # row 5개, col 3개
  print(arr)
  #[[0. 0. 0. 0. 0.]
  # [0. 0. 0. 0. 0.]]
  
  arr = np.zeros((2,5), dtype=np.int32)
  print(arr)
  #[[0 0 0 0 0]
  # [0 0 0 0 0]]
  ```

#### 2. ones

 * `array`에 1값으로 다채우므로써 사전할당 한다.

 * 입력값은 `zeros`와 같다.

   ```python
   arr = np.ones((3,4))
   print(arr)
   # [[1. 1. 1. 1.]
   # [1. 1. 1. 1.]
   # [1. 1. 1. 1.]]
   ```



#### 3. full

* `zeros`나 `ones`와 같이 원하는 값으로 사전할당할 수 있다.

* 입력값으로 원하는 array의 shape, 채울 value, dtype을 받는다.

  ```python
  arr = np.full((2,4),10**(-2))
  print(arr)
  #[[0.01 0.01 0.01 0.01]
  # [0.01 0.01 0.01 0.01]]
  
  arr = np.full((2,4),10**(-2), dtype=np.int32)  # 소수값을 int 취하면 소수점아래를 버림한다.
  #[[0 0 0 0]
  # [0 0 0 0]]
  ```

  

#### 4. empty

 * `zeros`와 달리 크기만 할당한다. ( `Matlab` 에서 `sparse`랑 유사해보인다.)

 * 입력값으로 원하는 array의 shape이 들어간다.

 * `zeros`에 비해 속도가 빠르다.

   ```python
   arr =np.empy((4,2))
   print(arr)
   # [[0.01 0.01]
   # [0.01 0.01]
   # [0.01 0.01]
   # [0.01 0.01]]
   ```





## 균등한 ndarray 

일정한 등분으로 생성되는 `ndarray`에 대해서 알아보자.

(`Matlab`에 있는 `linspace`와 `:` 와 같다.)

#### 1. arange

* `시작점 `, `끝점`,  `등분` 이 들어간다.

* `python`의 `range`와 비슷하다.

  ```python
  print(range(1,10,2)) # range(1, 10, 2)
  
  arr = np.arange(1,10,2)
  print(arr)           # [1 3 5 7 9]
  ```

  

#### 2. linsapce

 * `시작점`, `끝점`, `점의 개수`가 들어간다. 

 * `dtype` 설정을 줄 수 있다.

   ```python
   arr = np.array(0,1,5)
   print(arr)
   # [0.   0.25 0.5  0.75 1.  ]
   ```

   

   



