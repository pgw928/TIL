## ColumnTransformer

> 각 열에 대한 전처리(변환)을 하는 변환기들을 하나로 합쳐 한번에 변환시킬 수 있도록 해준다.



* 필요 library 불러오기

  ```python
  import pandas as pd
  import numpy as np
  import seaborn as sns
  from sklearn.linear_model import ElasticNet
  from sklearn.pipeline import make_pipeline, Pipeline
  from sklearn.preprocessing import StandardScaler, OneHotEncoder
  from sklearn.model_selection import train_test_split, GridSearchCV
  from sklearn.compose import ColumnTransformer
  
  import warnings
  warnings.simplefilter('ignore')
  ```

  * `ColumnTransformer`는 `sklearn`의 `compose`에 포함되어 있다.

  

* data 불러오기 및 처리

  ```python
  train_df = pd.read_excel('./data4/hyundaiCar.xlsx', sheet_name='train')
  test_df = pd.read_excel('./data4/hyundaiCar.xlsx', sheet_name='test')
  
  train_df = pd.read_excel('./data4/hyundaiCar.xlsx', sheet_name='train')
  test_df = pd.read_excel('./data4/hyundaiCar.xlsx', sheet_name='test')
  
  x_train, y_train = train_df.iloc[:, 1:], train_df['가격']
  x_test, y_test = test_df.iloc[:, 1:], test_df['가격']
  ```

  

* `ColumnTransformer`

  ```python
  ct = ColumnTransformer([('scaling', StandardScaler(), ['연비', '년식', '마력', '토크', '하이브리드', '배기량', '중량']),
                         ('onehot', OneHotEncoder(sparse=False), ['종류', '연료', '변속기'])])
  
  ```

  * 인자가 `list` 형태로 들어간다.
  * `list`에는 각 함수에 대해서 `tuple` 형태로 들어간다.
  * `tuple`에는 (함수별칭, 함수, 컬럼리스트) 형태로 들어간다.

  

* pipeline 생성

  ```python
  model = Pipeline([('ct', ct), ('clf', ElasticNet())])
  ```

  

* grid search

  ```python
  param_grid = {'clf__alpha':[0, 0.25, 0.5, 1, 2, 4, 16], 'clf__l1_ratio':[0, 0.25, 0.5, 0.75, 1]}
  grid = GridSearchCV(model, param_grid=param_grid, cv=5, scoring='r2')
  grid.fit(x_train, y_train)
  ```

  ```python
  ## 출력
  GridSearchCV(cv=5,
               estimator=Pipeline(steps=[('ct',
                                          ColumnTransformer(transformers=[('scaling',
                                                                           StandardScaler(),
                                                                           ['연비',
                                                                            '년식',
                                                                            '마력',
                                                                            '토크',
                                                                            '하이브리드',
                                                                            '배기량',
                                                                            '중량']),
                                                                          ('onehot',
                                                                           OneHotEncoder(sparse=False),
                                                                           ['종류',
                                                                            '연료',
                                                                            '변속기'])])),
                                         ('clf', ElasticNet())]),
               param_grid={'clf__alpha': [0, 0.25, 0.5, 1, 2, 4, 16],
                           'clf__l1_ratio': [0, 0.25, 0.5, 0.75, 1]},
               scoring='r2')
  ```

  

* 결과

  ```python
  print(grid.best_params_) # {'clf__alpha': 0.25, 'clf__l1_ratio': 0.25}
  print(grid.best_score_) # 0.7441481664137285
  ```

  ```python
  print(grid.best_estimator_.score(x_train, y_train)) # 0.8491233295265207
  print(grid.best_estimator_.score(x_test, y_test)) # 0.7066184827780425
  ```

  