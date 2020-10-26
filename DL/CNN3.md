# CNN 기초예제_TF1.15(MNIST)

> 기본 CNN을 이용해 mnist 예제를 예측해본다. 여기서는 jupyter notebook이 아닌 colab을 사용했다.



## Library

> 사용된 **Library**를 정의한다.

```python
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
```



## DataSet

> **DataSet**를 불러오고 preprocessing 을 진행한다.

```python
df = read_csv('/content/drive/My Drive/MachineLearning/data/mnist/train.csv')

x_data_train, x_data_test, t_data_train, t_data_test =\
train_test_split(df.drop('label', axis=1, inplace=False),
                 df['label'], test_size=0.3, random_state=0)

scaler = MaxMinScaler()
scaler.fit(x_data_train)
x_data_train_norm = scaler.transform(x_data_train)
x_data_test_norm = scaler.transform(x_data_test)

del x_data_train
del x_data_test

sess = tf.Session()

t_data_train_onehot = sess.run(tf.one_hot(t_data_train, depth=10))
t_data_test_onehot = sess.run(tf.one_hot(t_data_test, depth=10))
```



## CNN

> TF1.15를 가지고 CNN모델을 완성한다.

* placeholder 및 입력 데이터 형태 설정

```python
# placeholder
X = tf.placeholder(shape=(None,x_data_train_norm.shape[1]), dtype=tf.float32)
T = tf.placeholder(shape=(None,t_data_train_onehot.shape[1]), dtype=tf.float32)
drop_rate = tf.placeholder(dtype=tf.float32)

# 입력 데이터 형태 설정
x_img = tf.reshape(X,[-1 ,28 ,28 , 1]) # (개수, height, width, channel)
```



* convolution layer, Relu, pooling layer

```python
# convolution layer1
W1 = tf.variable(tf.random.normal([3,3 , 1, 32])) # (height,width,channel, 개수)

L1 = tf.conv2d(x_img, W1, strides=[1,1,1,1], pooling='SAME')
L1 = tf.nn.relu(L1)

# pooling layer1
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1] strides=[1,2,2,1], pooling='SAME')
print('L1의 shape : {}'.format(L1.shape)) # L1의 shape : (?, 14, 14, 32)

# convolution layer2
W2 = tf.variable(tf.normal.random([3,3,32,64]))

L2 = tf.nn.conv2d(L1, W2, strides=[1,1,1,1], pooling='SAME')
L2 = tf.nn.relu(L2)

# pooling layer2
L2 = tf.nn.max_pool(L2, ksize=[1,1,1,1], strides=[1,1,1,1], pooling='SAME')
print('L2의 shape : {}'.format(L2.shape)) # L2의 shape : (?, 7, 7, 64)
```



* FC layer

```python
# FC layer로 들어가기 위한 Flatten 과정
L2 = tf.reshape(L2,[-1, 7*7*64])

# Weight3 and bias
W3 = tf.get_varaible('weight3', shape=[7*7*64, 256], initializer=tf.contrib.layers.variance_scaling_initializer())
b3 = tf.Variable(tf.random.normal([256]), name='bias3')

# layer
_layer3 = tf.nn.relu(tf.matmul(L2,w3)+b3)
layer3 = tf.nn.dropout(_layer3, rate=drop_rate)

# Weight4 and bias
W4 = tf.get_initializer('weight4', shape=[256, 10], initializer=tf.contrib.layers.variance_scaling_initializer())
b4 = tf.Variable(tf.random.normal([10]), name='bias4')

# Hypothesis
logit = tf.matmul(layer3, W4) + b4
H = tf.nn.softmax(logit)

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_validatio_with_logits_v2(logits=logit, labels=T))

# train
train = tf.train.AdamOptimizer(learning_rate=1e-3).minimize(loss)

# parameter
num_of_epoch =200
batch_size= 100

def run_train(sess,train_x,train_t):
    print('###학습이 시작되요!!###')
    sess.run(tf.global_variables_initializer())
    
    total_batch = int(train_x.shape[0]/batch_size)
    
    for step in range(num_of_epoch):
        for i in range(total_batch):
            batch_x = train_x[i*batch_size:(i+1)*batch_size]
            batch_t = train_t[i*batch_size:(i+1)*batch_size]
            _, loss_val = sess.run([train, loss], feed_dict={X:batch_x,
                                                             T:batch_t,
                                                             drop_rate:0.4})
        if step % 20 == 0:
            print('loss : {}'.format(loss_val))
    print('###학습이 종료되요!!###')
```



* 결과

```python
result = run_train(sess, x_data_train_norm, t_data_train_onehot)
# ###학습이 시작되요!!###
# loss : 0.4871692657470703
# loss : 0.02252289280295372
# loss : 0.052905045449733734
# loss : 0.0018550120294094086
# loss : 3.7839847209397703e-05
# loss : 0.000732154177967459
# loss : 1.346974613625207e-06
# loss : 5.364403321550526e-08
# loss : 1.19209286886246e-09
# loss : 6.675698216440651e-08
# ###학습이 종료되요!!###

# Accuracy
predict = tf.argmax(H,1)

target_names ={'num 0','num 1','num 2','num 3','num 4','num 5','num 6','num 7','num 8','num 9'}
print(classification_report(t_data_test,
                            sess.run(predict,
                                     feed_dict={X:x_data_test_norm, 
                                                drop_rate:0 }),
                            target_names=target_names))  

#               precision    recall  f1-score   support
# 
#        num 0       0.99      0.99      0.99      1242
#        num 9       0.99      0.99      0.99      1429
#        num 8       0.98      0.99      0.99      1276
#        num 1       0.99      0.99      0.99      1298
#        num 3       0.99      0.98      0.98      1236
#        num 4       0.99      0.99      0.99      1119
#        num 5       0.99      1.00      0.99      1243
#        num 6       0.99      0.99      0.99      1334
#        num 7       0.99      0.98      0.99      1204
#        num 2       0.98      0.98      0.98      1219
# 
#     accuracy                           0.99     12600
#    macro avg       0.99      0.99      0.99     12600
# weighted avg       0.99      0.99      0.99     12600
```



