# 이미지 처리 및 Convolution

> CNN 코드에 들어가기 앞서 이미지 처리하는 한가지 방법에 대해서 알아본다.



## numpy를 이용한 이미지 데이터 및 필터 만들기

> image는  우리가 가로, 세로, color 수로 3차원이지만  이미지 개수 또한 제일 앞 차원에 추가해서 4차원 데이터로 만들어 사용한다. 즉, (이미지 개수, width, height, color 수) 로 표현된다.
>
> 또한 필터의 경우도 4차원이지만 image와 달리  (width, height, 필터의 channel, 필터의 개수)로 정의 된다.

### EXAMPLE

* 이미지 개수 : 1, 가로 : 3pixel, 세로 : 3pixel,  color 1개인 **image data**를 만들어 본다. 채워지는 값은 1로 채운다.  `img.shape=(1, 3, 3, 1)` 이 나와야한다.

  ```python
  import numpy as np
  # 뒤에서 부터 생각한다.
  # (,1)     => [1]
  # (,3,1)   => [[1],[1],[1]]  : [1] 이 3개
  # (,3,3,1) => [[[1],[1],[1]],[[1],[1],[1]],[[1],[1],[1]]]  : [[1],[1],[1]] 이 3개
  # (1, 3, 3, 1) => [[[[1],[1],[1]],[[1],[1],[1]],[[1],[1],[1]]]]
  img = np.array([[[[1],[1],[1]],[[1],[1],[1]],[[1],[1],[1]]]], dtype=np.float32)
  # dtype 명시 안하면 error 발생!!!
  
  print(img.shape) # (1, 3, 3, 1)
  ```



* Filter 만들기 :   가로길이 : 2, 세로길이: 2, 필처 채널 :1 , 필터 개수 :5 즉,`weight.shape = (2,2,1,5)` 

  ```python
  weight=np.array( [[[[1, 2, 3, 4, 5]],
  		           [[1, 2, 3, 4, 5]]],
          		  [[[1, 2, 3, 4, 5]],
            		   [[1, 2, 3, 4, 5]]]])
  print(weight.shape) # (2, 2, 1, 5)
  
  ```



* convolution 해보기 : `tensorflow`의 `nn.conv2d` 를 사용한다. 첫번째 인자로는 **이미지**, 두번째 인자로는 **filter**, 추가적으로 `strides`및 `padding`을 입력한다. 

  * `strides`의 경우 1차원의 4개이 성분을 입력하는데 첫 성분과 마지막 성분은 무조건 1이고

    가운데  진짜 stride가 들어간다.

  * `pading`의 경우 `VALID` 와 `SAME` 중에 padding을 원치 않으면 `VALID`값을 주고 같은 크기가 되게 만들때는 `SAME` 값을 입력한다.

  ```python
  result = tf.nn.conv2d(img, weight, strides=[1, 1, 1, 1], padding='VALID')
  sess = tf.Session()
  conv2d = sess.run(result)
  print(conv2d.shape)    # (1, 2, 2, 5)
  ```





## 이미지 처리하기

> 이미지 다루는 간단한 방법들에 대해서 알아본다.

#### 필요 Library

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # PIL : Python Imaging Libray, 이미지를 불러오기 위해 사용
```



#### 이미지 불러오기 및 픽셀

* 구글에서 원하는 이미지를 다운받아 불러온다.

```python
image = Image.open('./image/valencia.jpg')

plt.imshow(image)
plt.show()
```

![image-20201024032335976](markdown-images/image-20201024032335976.png)

* 이미지 사이즈 및 pixel로 변환

```python
print(image.size)        # (1024, 679)  : (가로, 세로)
pixel = np.array(image)
print(pixel.shape)       # (679, 1024, 3)  : (행(세로), 열(가로), 장수(color수))
```



#### 이미지 저장하기

* 이미지 객체의 정보를 이용하여 이미지를 저장한다.

```python
image.save('./image/my_picture.jpg')
```



#### 이미지 잘라내기

* `crop` 을 사용해 이미지를 잘라낸다. 이때 `tuple`로 데이터가 입력 되며 **(가로시작, 세로시작, 가로끝, 세로끝)**  형식의 `tuple` 을 인자로 갖는다.

```python
crop_image = image.crop((400, 150, 800, 400))
plt.imshow(crop_img)
plt.show()
```

![image-20201024040639845](markdown-images/image-20201024040639845.png)



#### 이미지 크기 바꾸기

* `resize` method를 사용해 바꿀 수 있다. 마찬가지로 `tuple` 형태로 입력한다.

```python
resized_image = image.resize((int(image.size[0]/8), (int(image.size[1]/8))))
plt.imshow(resized_image)
plt.show()
```

![image-20201024191411276](markdown-images/image-20201024191411276.png)



#### 이미지 회전하기

* `rotate` method를 이용해서 회전한다. 입력값으로  60분법을 사용하면 -값을 시계방향 회전으로 정의된다.

```python
rotated_image = image.rotate(-90)
plt.imshow(rotated_image)
plt.show()
```

![image-20201024191805639](markdown-images/image-20201024191805639.png)





#### 이미지 흑백으로 만들기

* pixel값을 이용해서 color 이미지의 평균값으로 가져온다. 그러나 이거 같은 경우 3장이기 때문에 보여지는것이 흑백이미지일 뿐이다.

```python
grey_pixel = pixel[:]
print(grey_pixel.shape)
for i in range(grey_pixel.shape[0]):
    for j in range(grey_pixel.shape[1]):
        grey_pixel[i,j,:] = grey_pixel[i,j,:].mean()

plt.imshow(grey_pixel)
plt.show() 
```

![image-20201024193811480](markdown-images/image-20201024193811480.png)

* 평균값으로 처리된것의 한장을 가져와 `imshow`의  `cmap=grey` 를 option으로 흑백 이미지를 가져온다.

```python
plt.imshow(grey_pixel[:,:,0:1], cmap='gray')  # grey_pixel[:,:,0] 으로 가져오면 shape이 2D가 된다.
plt.show()
```

![image-20201024194039225](markdown-images/image-20201024194039225.png)