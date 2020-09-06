# 여러가지 ndarry-(2)[random값 이용-1] 

> random값을 이용해 ndarray를 만드는 방법을 소개한다. 총 5가지 방법이다.



## 1. random.normal

* 정규분포 확률밀도함수에서 실수 표본을 추출해 ndarry를 만든다.

* `평균`, `표준편차`, `shape` 을 입력값으로 받는다.

  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  
  mean = 50
  std = 2
  arr = np.random.normal(mean, std, (10000))
  #[50.84878324 52.62002286 49.79075786 ... 48.81352882 50.85878254
  # 52.22862578] : 결과값으로 앞의 3개 뒤의 3개 나온다.
  plt.hist(arr, bins =100) # bin : 구간 개수
  plt.show()
  ```

![정규분포](C:\Users\User\Desktop\GIT\TIL\markdown-images\정규분포.PNG)

  * 정규분포이기 때문에  평균 근처로 갈수록 더 많은 random값들이 뽑혔다.

## 2. random.randn

   * 표준정규분포 확률밀도함수에서 난수를 추출한다.

   * 입력값으로 `tuple` 없이  `shape`을 입력한다.

     ```python
     arr = np.random.rand(1000)
     print(arr)
     #[-0.20012848 -0.73003218 -0.41702728 ... -0.75750826 -1.67561455
     # -0.75460698]
     
     plt.hist(arr, bins=100)
     plot.show()
     ```

        				 	![표준정규분포](C:\Users\User\Desktop\GIT\TIL\markdown-images\표준정규분포.PNG)

   

## 3. random.rand

* 균등분포에서 [0, 1) 범위에서 랜덤값을 추출한다.

* 입력값으로 `tuple` 없이 `shape`을 입력한다.

   ```python
  arr = np.random.rand(10000)
  print(arr)
  plt.hist(arr, bins=100)
  plot.show()
  ```

  ![rand](C:\Users\User\Desktop\GIT\TIL\markdown-images\rand.PNG)

  

## 4. random.randint

* 균등분포에서 확률밀도함수에서 난수를 추출하는데 정수값으로 랜덤값을 추출한다.

* 입력값으로 랜덤값의 `범위`와 `shape`을 받는다.

  ```python
  arr = random.randint(-50, 100, (10000))
  print(arr)
  plt.hist(arr, bins=100)
  plt.show()
  ```

  ![randint](C:\Users\User\Desktop\GIT\TIL\markdown-images\randint.PNG)

  

## 5. random.random

* **3** 의 `rand.rand`와 같이 균등분포에서 [0, 1) 범위에서 랜덤값을 추출한다.

* **3**과 달리 입력으로 `tuple`을 포함한 `shape`을 받는다.

  ```python
  arr = np.random.random((10000))
  print(arr)
  plt.hist(arr, bins=100)
  plt.show()
  ```

  ![random](C:\Users\User\Desktop\GIT\TIL\markdown-images\random.PNG)



