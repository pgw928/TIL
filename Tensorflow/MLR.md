# MLR(Multi Linear Regression)-(예제)

> `TF2.x`를 사용한 Multi Linear Regression 모델을 가지고 Ozone dataset 예제를 해결해 본다.

`Solar.R`, `Wind`, `Temp`에 따른 `Ozone`값을 예측해본다.



## Dataset 및 필요 Library

* Library

```python
import numpy as np
import pandas as pd
import tensorflow as tf

from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.neightbors import KNeighborsRegressor

from tensorflow.keras.models import Sequential
from tensorflow.keras.layer import Flatten, Dense
from tensorflow.keras.optimizers import SGD

from sklearn.linear_model import LinearRegression
```

* Dataset

```python
df = pd.read_csv('./data/ozone.csv')
training_data = df[['Solar.R','Wind','Temp','Ozone']]
display(training_data.head())

x_data = training_data[['Solar.R', 'Wind', 'Temp']]
t_data = training_data['Ozone']
```

![image-20201013200128813](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20201013200128813.png)



## Preprocessing

> 결측치 보간, 이상치 제거, 정규화를 진행한다.

* 결측치 : 독립변수에 대해서는 median값을 종속변수에 대해서는 KNN을 사용한다.

  * 결측치 확인

  ```python
  print(training_data.isnull().sum())
  # Solar.R     7
  # Wind        0
  # Temp        0
  # Ozone      37
  # dtype: int64
  ```

  * 독립변수의 결측치 : median 값을 사용해 처리한다.

  ```python
  for col in x_data.columns:
      m = np.nanmedian(x_data[col])
      x_data[col] = x_data[col].fillna(m)
  ```



* 이상치 제거 : z-score를 통해 이상치를 평균값으로 대체한다.

```python
z_score_threshold = 1.8
for col in x_data.columns:
    col_mean = np.mean(x_data[col].loc[~(np.abs(stats.zscore(x_data[col])) > z_score_threshold)])
    x_data[col].loc[np.abs(stats.zscore(x_data[col])) > z_score_threshold] = col_mean
```



* 정규화 :  MinMaxScaler를 이용해 정규화과정을 거친다.

```python
scaler_x = MinMaxScaler() 
scaler_t = MinMaxScaler()

scaler_x.fit(x_data)
scaler_t.fit(t_data.values.reshape(-1,1))  # 반드시 2차원이 들어와야한다.

x_data_norm = scaler_x.transform(x_data)
t_data_norm = scaler_t.transform(t_data.values.reshape(-1,1)).ravel() 
# 밑에서 1차원으로 사용되기 때문에 ravel() 처리를 해준다.
```



* 종속변수에 대한 결측치 보간 : K-Nearest Neighbor 를 이용해 종속변수 결측치를 보간한다.

```python
x_data_train_norm = x_data_norm[~np.isnan(t_data_norm)]
t_data_train_norm = t_data_norm[~np.isnan(t_data_norm)]

knn_regressor = KNeighborsRegressor(n_neighbors=2)
knn_regressor.fit(x_data_train_norm, t_data_train_norm)

knn_predict = knn_regressor.predict(x_data_norm[np.isnan(t_data_norm)])
t_data_norm[np.isnan(t_data_norm)] = knn_predict
```



## 학습 진행

> `TF2.xx`로 학습을 진행해본다.

* model 생성 및 layer 생성

```python
keras_model = Sequential()      							  # 생성
keras_model.add(Flatten(input_shape=(x_data_norm.shape[1],))) # input layer
keras_model.add(Dense(1, activation='mse'))					  # output layer
```

* model compile

```python
keras_model.compile(optimizer=SGD(learning_rate=1e-2), loss='mse')
```

* 학습

```python
keras_model.fit(x_data_norm, t_data_norm, epochs=5000, verbose=0)
```

* prediction

```python
test_data = [[310, 15, 80]]
result = keras_model.predict(scaler_x.transform(test_data))
scaled_result = scaler_t.inverse_transform(result)
print('tensorflow 결과 : {}'.format(scaled_result))
```

* 결과

```python
# tensorflow 결과 : [[38.711735]]
```



## sklearn 과 비교

> 결과를 확인하기 위해 sklearn의 결과와 비교해 본다.

* 코드 구현

```python
sklearn_model = LinearRegression()
sklearn_model.fit(x_data_norm, t_data_norm)
```

* prediction

```python
test_data = [[310, 15, 80]]
result = sklearn_model.predict(train_data).reshape(-1,1)
scaled_result = scaler_t.inverse_trainsfomr(result)
print('sklearn 결과 : {}'.format(scaled_result))
```

* 결과

```python
# sklearn 결과 : [[38.75927452]]
```



## 결론

> `sklearn`과 `tensorflow`의 결과는 비슷하게 나왔다.