## pandas_profileReport

> Auto EDA 라이브러리를 간단히 소개한다.



* ### Data

  ```python
  BASE_DIR = './data' 
  train_path = os.path.join(BASE_DIR, 'train.csv')
  train = pd.read_csv(train_path)
  train.head()
  ```

  ![image-20210811021210946](markdown-images/image-20210811021210946.png)



* ### 설치

  ```python
  pip install pandas_profiling
  ```

  

* ### 불러오기 및 실행

  ```python
  from pandas_profiling import ProfileReport
  profile = ProfileReport(train, title='신용카드 사용 연체 예측')
  profile
  ```

  * 아래와 같이 결과를 불러오는 진행과정을 알려준다.

    ![image-20210811021415784](markdown-images/image-20210811021415784.png)

  * 네비게이션

    ![image-20210811021533566](markdown-images/image-20210811021533566.png)



* ### Overview

  * Overview : 데이터 정보를 간단히 알려준다.

    ![image-20210811021720834](markdown-images/image-20210811021720834.png)

   * Warnings : 데이터의 문제점을 알려준다.

     ![image-20210811021816233](markdown-images/image-20210811021816233.png)

* Variables : 컬럼명 데이터 정보를 알려준다.

  ![image-20210811022029751](markdown-images/image-20210811022029751.png)

* Interactions : 두 변수간의 관계를 볼 수 있다.

  ![image-20210811022329661](markdown-images/image-20210811022329661.png)

* Correlations : 상관관계를 볼 수 있다.

  ![image-20210811022417354](markdown-images/image-20210811022417354.png)

