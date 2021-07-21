## GridSearchCV

> 더 좋은 매개변수를 찾기 위해 사용된다. pipeline과 조합되어 사용될 수 있다.



* 필요한 library

  ```python
  import numpy as np
  import pandas as pd
  from sklearn.preprocessing import StandardScaler
  from sklearn.datasets import load_boston
  from sklearn.pipeline import make_pipeline, Pipeline
  from sklearn.model_selection import train_test_split, GridSearchCV
  from sklearn.linear_model import ElasticNet
  ```

  * `GridSearchCV`는 `sklearn`의 `model_selection`에 포함되어 있다.

* data : boston data를 사용한다.

  ```python
  boston = load_boston()
  
  boston.keys()
  # dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
  
  type(boston['data'])
  # numpy.ndarray
  ```

    ```python
    boston_df = pd.DataFrame(boston['data'])
    boston_df['MEDV'] = boston['target']
    boston_df.head()
    ```

    ![image-20210722020654112](markdown-images/image-20210722020654112.png)

    ```python
    x_data, y_data = boston_df.iloc[:,:-1].values, boston_df['MEDV'].values
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=1)
    ```

* make_pipeline으로  model pipeline 생성

  ```python
  model = make_pipeline(StandardScaler(), ElasticNet())
  model.steps
  # [('standardscaler', StandardScaler()), ('elasticnet', ElasticNet())]
  ```

* `GridSearchCV`를 이용해 모델 학습 및 최적의 parameter 찾기

  ```python
  param_grid = {'elasticnet__alpha':[0, 0.25, 0.5, 1, 2, 4, 16], 'elasticnet__l1_ratio':[0, 0.25, 0.5, 0.75, 1]}
  grid = GridSearchCV(model, param_grid=param_grid, cv=5, scoring='r2')
  grid.fit(x_train, y_train)
  
  ## ------ 출력 ------
  GridSearchCV(cv=5,
               estimator=Pipeline(steps=[('standardscaler', StandardScaler()),
                                         ('elasticnet', ElasticNet())]),
               param_grid={'elasticnet__alpha': [0, 0.25, 0.5, 1, 2, 4, 16],
                           'elasticnet__l1_ratio': [0, 0.25, 0.5, 0.75, 1]},
               scoring='r2')
  ```

  * parame_grid에 `dict`로 변수에 대한 값을 `list` 형태로 건내준다. `dict`의 `key`는 **별칭__parameter명** 으로 작성한다. 여기서 언더바 두개이다.

  ```python
  print(grid.best_params_) # {'elasticnet__alpha': 0, 'elasticnet__l1_ratio': 0}
  print(grid.best_score_) # 0.7025123301096212
  ```

* `best_estimator_`로 score 확인

  ```python
  print(grid.best_estimator_.score(x_train, y_train)) # 0.7293585058196337
  print(grid.best_estimator_.score(x_test, y_test)) # 0.7634174432138474
  ```

  

