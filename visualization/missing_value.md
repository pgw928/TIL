# 결측치 시각화

> 결측치 시각화에 대해서 다룬다.

* ### 사용 데이터

  ```python
  features.head()
  ```

  ![image-20210609160907729](markdown-images/image-20210609160907729.png)



## 1. seaborn 사용

* ### libary 호출

  ```python
  import seaborn as sns
  ```

  

* ### heatmap

  ```python
  sns.heatmap(features.isnull(), cmap=False)
  ```

  ![image-20210609162751075](markdown-images/image-20210609162751075.png)





## 2. missingo 사용

* ### library 호출

  ```python
  import missingno as msno
  ```



* ### matrix

  ```python
  msno.matrix(features)
  plt.show()
  ```

  * 매트릭스 형태로 결측치를 시각화한다.

  ![image-20210609161154589](markdown-images/image-20210609161154589.png)



* ### Bar Chart

  ```python
  msno.bar(features)
  plt.show()
  ```

  ![image-20210609161601781](markdown-images/image-20210609161601781.png)



#### 참고

https://github.com/ResidentMario/missingno

