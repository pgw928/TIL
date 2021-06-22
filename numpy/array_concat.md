# 배열 붙이기(1)

> numpy의 배열을 붙이는 함수  `np.hstack`, `np.vstack`, `np.concatenate`에 대해서 알아본다.



* ### 데이터

  ```python
  a = np.array([1, 2, 3, 4, 5])
  b = np.array([6, 7, 8, 9, 10])
  
  c = a.reshape(1, -1)
  d = b.reshape(1, -1)
  ```

  

* ### 1차원 array 열로 붙이기

  * np.hstack

    ```python
    np.hstack((a, b))
    # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    ```

  * np.concatenate

    ```python
    np.concatenate((a, b), axis=0)
    # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    ```

    

  

* ### 1차원 array 행으로 붙이기(2차원으로)

  * np.vstack

    ```python
    np.vstack((a, b))
    # array([[ 1,  2,  3,  4,  5],
    #        [ 6,  7,  8,  9, 10]])
    ```

    



* ### 2차원 array 열로 붙이기

  * np.hstack

    ```python
    np.hstack((c, d))
    # array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]])
    ```

  * np.concatenate

    ```python
    np.concatenate((c, d), axis=1)
    # array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]])
    ```

  

* ### 2차원 array 행으로 붙이기

  * np.vstack

    ```python
    np.vstack((c, d))
    # array([[ 1,  2,  3,  4,  5],
    #        [ 6,  7,  8,  9, 10]])
    ```

  * np.concatenate

    ```python
    np.concatenate((c, d), axis=0)
    # array([[ 1,  2,  3,  4,  5],
    #        [ 6,  7,  8,  9, 10]])
    ```

    