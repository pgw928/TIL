#  Indexing 및 Slicing

> 데이터를 불러올 때 전체를 가져오는게 아니라 일부만 가져올 때 `indexing` 또는 `slicing` 이 사용된다.
>
> `ndarray` 는 어떻게 `indexing` 과 `slicing` 을 하는지 설명한다.



## 기본 Indexing  및 Slicing

> `python` 의 `list` 또는 `tuple` 과 비슷하지만 약간의 차이가 존재한다.

#### 1. Indexing 

* 2가지 방법이 기본적이다.
  * 이중 list로 생각해서 `python` 의 `list` 와 똑같이 구할 수 있다.

    ```python
    arr = np.arange(0,6).reshape((2,3)).copy()
    print(arr)        #[[0 1 2]
    			      # [3 4 5]]
    print(arr[1][1])  # 4
    print(arr[1][2])  # 5
    ```

  * matrix coordinate로 생각해서 구할 수 있다.

    ```python
    print(arr[1,1])   # 4
    print(arr[1,2])   # 5
    ```



#### 2. Slicing

* 1-dimensional  `ndarray` 

  * `python` 의 `list`와 같다.

    ```python
    arr = np.arange(0,6)
    print(arr)         # [0 1 2 3 4 5]
    print(arr[1:3])    # [1 2]
    ```

* 2-dimensional `ndarray`

   * 1-dimensional `row ` 뽑아내기

     ```python
     np.random.seed(0)
     arr = np.random.randint(0,12,(3,4))
     print(arr)          # [[ 5  0  3 11]
     					#  [ 3  7  9  3]
     					#  [ 5  2  4  7]]
     print(arr[2])       # [5 2 4 7]
     print(arr[0])       # [ 5  0  3 11]
     ```

  * 1-dimensional `col` 뽑아내기

    ```python
    print(arr[0:,1])    # [0 7 2]
    print(arr[0:,2])    # [3 9 4]
    ```

  * 부분 2-dimensional `ndarray` 뽑아내기

    ```python
    print(arr[1:,1:3])  # [[7 9]
    				    #  [2 4]]
        
    ## 다음과 같이 indexing과 같이 생각하면 원하는것을 뽑아내지 못한다.
    print(arr[1:])      # [[3 7 9 3]
     					#  [5 2 4 7]]
    print(arr[1:][1:])  # [[5 2 4 7]]
    # arr[1:]이 2-dimensional ndarry이기 때문에 
    # arr[1:][1:] 도 다시 2-dimensional ndarray가 된다.
    ```

    

## Boolean indexing

> `True`, `False`로 구성된 boolean mask를 이용하여 `True`에 해당하는 index만을 조회하는 방식이다.

```python
import numpy as np

np.random.seed(1)
arr = np.random.randint(0,10,(7,))
print(arr)                   # [5 8 9 5 0 0 1]
print(arr % 2 == 0)          # [False  True False False False]
print(arr[arr % 2==0])       # [8 0 0]
```



## Fancy indexing

> `ndarray`에 `index` 배열을 전달하여 배열요소를 참조하는 방식이다.

* 1-dimension (결과가 1 dimension)

  ```python
  import numpy as np
  
  arr= np.arange(0,12).reshape(3,4).copy()
  print(arr)              # [[ 0  1  2  3]
  						#  [ 4  5  6  7]
  						#  [ 8  9 10 11]]
  print(arr[[1,2],2])     # [ 6 10]
  print(arr[2,[1,2]])     # [ 9 10]  
  print(arr[[0,2],2:3])   # [[ 2]
  						#  [10]]
  ```

* 2-dimension (결과가 2 dimension)

  * fancy indexing은 `row`,  `column` 모두 동시에 사용할 수 없다.  다음 예제를 보면 알 수 있다.

    ```python
    print(arr)              # [[ 0  1  2  3]
    						#  [ 4  5  6  7]
    						#  [ 8  9 10 11]]
    print(arr[[1,2],[1,2]]) #  [ 5 10]       
    # 위에서 의도한 것은 [[5 6]
    #				   9 10]]
    ```

  *  해결 방법-1 : 두번에 걸처서 진행한다.

    ```python
    print(arr[[1,2]])           # [[ 4  5  6  7]
    							#  [ 8  9 10 11]]
    print(arr[[1,2]][:,[1,2]])  # [[ 5  6]
    							# [ 9 10]]
    ```
    
  * 해결 방법-2 :  ix_ 함수를 사용한다
  
    ```python
    print(arr[np.ix_([1, 2], [1, 2])])   # [[ 5  6]
    									 # [ 9 10]]
    print(np.ix_([1, 2], [1, 2]))        # (array([[0],
            							 #	      [2]]), array([[1, 3]]))
    ```
  
    