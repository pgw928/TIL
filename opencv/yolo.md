# OpenCV를 사용한 YOLO Object Detection(1)

> OpenCV를 활용해 YOLO( You Only Look Once)구현 방법에 대해서 다룬다.



## 사용하는 Library

> 사용하는 Libray를 나열한다.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```



##  필요한 files

> YOLO를 사용하기 위해 다운받아야 할 파일들을 나열한다.

```bash
yolo test.ipynb
yolo files 
├── coco.names                  # YOLO가 detect할 수 있는 물체들의 이름들을 포함한다. coco : dataset 이름이다.
├── room_ser.jpg			    # YOLO Test sample 이미지이다.
├── yolo_object_detection.py    # 없어도 되는 파일???
├── yolov3.cfg 				    # configuration file, 알고리즘에 모든 설정이 있다.
└── yolov3.weights				# 이미 학습이 완료된 model이다.
```



##  YOLO 로드

>

```python
net = cv2.dnn.readnet()
```

