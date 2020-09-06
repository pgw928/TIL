# 여러가지 ndarrya-(3)[random값 이용-2]

> random 값 함수의 추가적인 `method`에 대해서 언급한다.



## 1. random.seed

* 난수의 재현 : seed에 값을 주어 랜던값을 고정한다.

  ```python
  np.random.seed(0)
  arr = np.random.randint(0,100,(10))
  print(arr)    # [44 47 64 67 67  9 83 21 36 87]
  
  np.random.seed(5)
  arr = np.random.randint(0,100,(10))
  print(arr)    # [99 78 61 16 73  8 62 27 30 80]
  ```



## 2 . random.shuffle

* 숫자를 `permutation` 또는 `shuffle` 한다.

  ```python
  arr = np.arange(10)
  print(arr)    # [0 1 2 3 4 5 6 7 8 9]
  np.random.shuffle(arr)
  print(arr)    # [6 2 9 8 4 3 0 5 1 7]
  ```



## 3. random.choice

 * 일부를 무작위로 선택하는 즉,sampling 기능을 수행한다.

 * 입력값으로  `array`, `size`, `replace`, `p` 값을 받는다.

    * array : array 또는 정수값이 온다. 정수값일 경우 arange(정수) 가 된다.
   * size : 표본(sample)의 개수이다.
   * replace : 복원 추출(`True`), 비복원 추출(`False`)을 선택한다. 
   * p : `array` element의 추출 확률값을 부여한다.

   ```python
   arr = np.random.choice(5,5,replace=False) # shuffle기능과 같아짐
   print(arr)    # [1 0 2 4 3]
   
   arr =np.random.choice(5, 10, replace=True, p=[0.2, 0, 0.3, 0.4, 0.1] )
   print(arr)
   ```

   