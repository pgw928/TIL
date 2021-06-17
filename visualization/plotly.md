# plotly

> 데이터 시각화의 high-level interface 로 파이썬의 대표적인 interactive 시각화 도구이다.



* ### 내장 데이터 가져오기

  ```python
  import plotly.express as px
  df = px.data.stocks()
  df
  ```

  ![image-20210617161830735](markdown-images/image-20210617161830735.png)

  * FAANG + MSFT 주식 데이터이다.

  

* ### 데이터 전처리

  * 날짜 컬럼 → index

    ```python
    df.set_index('date', inplace=True)
    df
    ```

    ![image-20210617174228736](markdown-images/image-20210617174228736.png)

  * 전체 data에 -1 연산

    ```python
    df_1 = df - 1
    df_1
    ```

    ![image-20210617174454768](markdown-images/image-20210617174454768.png)

  * column명 company로 설정

    ```python
    df_1.columns.name = 'company'
    df_1
    ```

    ![image-20210617174602947](markdown-images/image-20210617174602947.png)

* bar plot

  * 구글 수익률 그래프

    ```python
    px.bar(df_1, x=df_1.columns, y='GOOG')
    ```

    
