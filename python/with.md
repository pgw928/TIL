# with문

> 자원을 획득하고 사용 후 반납하는 경우 주로 사용된다. 



* 자원을 획득한다.
* 자원을 사용한다.
* 자원을 반납한다.





예를 들어 파일을 열고 사용했다면 다른 process를 위해 닫고 자원을 반납해야 한다.

이것을 수동으로 코딩할 수 있지만 with문을 사용하면 자동으로 처리해준다.

일반적으로 다음과 같은 문법을 지닌다.

```python
with open(file url, 모드) as f: # as f는 파일 객체를 f 로 쓴다는 뜻
    f 관련 처리
```

위에 나와 있는 모드는 밑에의 옵션이 주로 사용 된다.

* `'r'`  : 읽기 모드, 파일을 읽을 때 사용된다.
* `'w'`  : 쓰기 모드, 파일에 쓸 때 사용하면 파일이 이미 동일한 이름으로 존재하면 덮어쓰기 해버린다.
* `'a'`  : 추가 모드, 존재하는 파일에 추가할 때 사용하면 파일이 없다면 생성한다.

더많은 옵션이 있지만 현재로는 생략한다.



## ex1)

> `readlines()` 함수 활용한다. `readlines()`은 파일을 한 줄 한줄 읽어 모두 리스트의 원소로 만들어준다.
>
> 참고로 `readline()`는 `readline()`과 달리 한줄 씩 뽑아준다.(ex> 두번 `f.readline() ` 입력하면 첫번째 줄과 두번째 줄의 값이 나온다.)

* `strip()` 사용

```python
with open('./yolo files/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines]
    print(classes)  
```

```python
['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
```

* `strip()` 사용안하면

```python
with open('./yolo files/coco.names', 'r') as f:
    print(f.readlines())
```

```python
['person\n', 'bicycle\n', 'car\n', 'motorbike\n', 'aeroplane\n', 'bus\n', 'train\n', 'truck\n', 'boat\n', 'traffic light\n', 'fire hydrant\n', 'stop sign\n', 'parking meter\n', 'bench\n', 'bird\n', 'cat\n', 'dog\n', 'horse\n', 'sheep\n', 'cow\n', 'elephant\n', 'bear\n', 'zebra\n', 'giraffe\n', 'backpack\n', 'umbrella\n', 'handbag\n', 'tie\n', 'suitcase\n', 'frisbee\n', 'skis\n', 'snowboard\n', 'sports ball\n', 'kite\n', 'baseball bat\n', 'baseball glove\n', 'skateboard\n', 'surfboard\n', 'tennis racket\n', 'bottle\n', 'wine glass\n', 'cup\n', 'fork\n', 'knife\n', 'spoon\n', 'bowl\n', 'banana\n', 'apple\n', 'sandwich\n', 'orange\n', 'broccoli\n', 'carrot\n', 'hot dog\n', 'pizza\n', 'donut\n', 'cake\n', 'chair\n', 'sofa\n', 'pottedplant\n', 'bed\n', 'diningtable\n', 'toilet\n', 'tvmonitor\n', 'laptop\n', 'mouse\n', 'remote\n', 'keyboard\n', 'cell phone\n', 'microwave\n', 'oven\n', 'toaster\n', 'sink\n', 'refrigerator\n', 'book\n', 'clock\n', 'vase\n', 'scissors\n', 'teddy bear\n', 'hair drier\n', 'toothbrush\n']
```





## ex2)

> tensorflow gpu 를 사용할 때도 사용된다.

```pthon
with tf.device('/device:GPU:0'):
	model_base = InceptionResNetV2(weights='imagenet',
                       include_top=False,
                       input_shape=(75, 75, 3))
   	model_base.summary()
	
```

