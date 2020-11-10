# GPU 할당 코드

> GPU 사용시 메모리 할당 하는 코드에 대해서 알아본다.

```python
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    # 특정 GPU에 7000GB 메모리만 할당하도록 제한
    try:
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=7000)])
    except RuntimeError as e:
    # 프로그램 시작시에 가상 장치가 설정되어야만 합니다
        print(e)
```



사용시 다음과 같이 `with`문 안에 model을 만든다.

```python
with tf.device('/device:GPU:0'):

    model_base = InceptionResNetV2(weights='imagenet',
                       include_top=False,
                       input_shape=(75, 75, 3))
    model_base.summary()

```





