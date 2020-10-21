# TF2(relu,he's initialization , dropout)(mnist 예제)

> **TF2**를 활용해 DNN을 구현한다. 여기서 주목해야 할 점은 activation function으로 **relu**를, 초기값 설정을 위해 **he's initialization** 방법을, overfitting을 막기 위해 `dropout`을 사용하는것에 초점을 둔다.



## Library 및 Training_data

* library

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

from sklearn.preprocessing import MinMaxScaler     
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
```

* DataSet

```python
df = pd.read_csv('./data/mnist/train.csv')

# Data Split
x_data_train, x_data_test, t_data_train, t_data_test = \
train_test_split(df.drop('label', axis=1, inplace=False), df['label'], test_size=0.3, random_state=0)
# Min-Max Normalization
scaler = MinMaxScaler()  
scaler.fit(x_data_train)
x_data_train_norm = scaler.transform(x_data_train)
x_data_test_norm = scaler.transform(x_data_test)

del x_data_train
del x_data_test
```



## 모델 생성 및 학습

* model 생성 및 compile

```python
keras_model = Sequential()
keras_model.add(Dense(256, activation='relu', kernel_initializer='he_uniform' input_shape=(x_data_train_norm ,)))
keras_model.add(dropout(0.3))
keras_model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
keras_model.add(dropout(0.3))
keras_model.add(Dense(10, activation='softmax', kernel_initializer='he_uniform'))

keras_model.compile(optimizer = Adam(learninig_rate=1e-2),
                    loss = 'sparse_categorical_crossentropy',
                    accuracy = ['sparse_categorical_accuracy'])
```

* 학습

```python
history =keras_model.fit(x_data_train_norm, t_data_train, epochs=100, batch_size=128, validataion_split=0.3 ,verbose=0 )
```

* 결과

```python
result = tf.argmax(keras_model.predict(x_data_test_norm), axis=1)
print(classification_report(t_data_test, result))
#               precision    recall  f1-score   support
# 
#            0       0.98      0.97      0.97      1242
#            1       0.98      0.98      0.98      1429
#            2       0.97      0.97      0.97      1276
#            3       0.98      0.96      0.97      1298
#            4       0.97      0.97      0.97      1236
#            5       0.97      0.96      0.97      1119
#            6       0.97      0.98      0.98      1243
#            7       0.97      0.97      0.97      1334
#            8       0.92      0.95      0.93      1204
#            9       0.96      0.95      0.95      1219
# 
#     accuracy                           0.97     12600
#    macro avg       0.97      0.97      0.97     12600
# weighted avg       0.97      0.97      0.97     12600
```

* 그래프로 accuracy 확인

```python
plt.plot(history.history['sparse_categorical_accuracy'])
plt.plot(history.history['val_sparse_categorical_accuracy'])
plt.show()
```

![image-20201021032037441](markdown-images/image-20201021032037441.png)