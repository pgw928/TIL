# XOR 학습시키기(TF1.xx)

> **TF1.15**를 사용한 **DNN** 모델을 만든다.



## Library

> 사용한 **Library**를 나열한다.

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
```





## 학습 진행

> `TF1.15`로 학습을 진행해본다.

* **XOR** DataSet

```python
x_data = np.array([[0,0],[1,0],[0,1],[1,1]], dtype=np.float32)
t_data = np.array([[0],[1],[1],[0]], dtype=np.float32)
```




* `placeholder`, `weight`, `bias`, `hyperthesis`, `logit`

```python
X = tf.placeholder(shape=[None, x_data.shape[1]], dtype=tf.float32)
T = tf.placeholder(shape=[None,1], dtype=tf.float32)

W2 = tf.Variable(tf.random.normal([x_data.shape[1], 100]), name='weight2')
b2 = tf.Variable(tf.random.normal([1]), name='bias2')
layer2 = tf.sigmoid(tf.matmul(X,W2)+b2)

W3 = tf.Variable(tf.random.normal([100,6]), name='weight3')
b3 = tf.Variable(tf.random.normal([6]), name='bias3')
layer2 = tf.sigmoid(tf.matmul(layer2,W3)+b3)

W4 = tf.Variable(tf.random.normal([6,1]), name='weight4')
b4 = tf.Variable(tf.random.normal([1]), name='bias4')

logit = tf.matmul(layer2, W4) + b4
H = tf.sigmoid(logit)
```



* `loss`, `train`, `session`

```python
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=T))

train = tf.train.GradientDescentOptimizer(learning_rate=1e-1).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
```



* 학습 진행

```python
for step in range(30000):
    _, loss_val = sess.run([train, loss], feed_dict={X:x_data, T:t_data})
    if step%3000==0:
	    print('loss : {}'.format(loss_val))
```



* 결과

```python
accuracy = tf.cast(H>=0.5, dtype=tf.float32)
result = sess.run(accuracy, feed_dict={X:x_data})
print(classification_report(t_data,result))
```

