# DataFrame의 결합(merge)(2)

>두 `DataFrame`을 어떠한 column을 기준으로 결합(join)할때 두 가지 상황에서 `merge`하는 법에 대해 알아본다.



## 1.  기준이 되는 column 명이 다를때

> 기준이 되고자 하는 `column` 명이 다를때 해결하는 방법에 대해서 알아본다.

```python
import numpy as np
import pandas as pd 

data1 = {'학번' : [1, 2, 3, 4],
        '이름' : ['이지안','박동훈','이순신','강감찬'],
        '학년' : [2, 4, 1, 3]}


data2 = {'학생학번' : [1, 2, 4 ,5],
         '학과' : ['CS','MATH','MATH', 'CS'],
         '학점' : [3.4, 2.9, 4.5, 1.2]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

display(df1)
display(df2)
```

![image-20200916224953489](markdown-images/image-20200916224953489.png)

![image-20200916225011150](markdown-images/image-20200916225011150.png)

* 결합을 할 때 `on` keyword 대신 `left_on` 과 `right_on` keyword를 입력해서 각 기준 `column` 을 입력할 수 있다.

```python
result = pd.merge(df1, df2, left_on='학번', right_on='학생학번', how='inner')
display(result)
# df1의 학번과 df2의 학생학번 기준으로 교집합 연산을 한다.
```

![image-20200916215924978](markdown-images/image-20200916215924978.png)



## 2. DataFrame의 column과 index를 이용한 merge

> DataFrame의 column 이나 index를 이용해 merge 가 가능하다.

```python
import numpy as np
import pandas as pd 


data1 = {'학번' : [1, 2, 3, 4],
        '이름' : ['이지안','박동훈','이순신','강감찬'],
        '학년' : [2, 4, 1, 3]}


data2 = {'학과' : ['CS','MATH','MATH', 'CS'],
         '학점' : [3.4, 2.9, 4.5, 1.2]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2, index=[1,2,4,5])  # 학번을 index로 사용
```

![image-20200916225627910](markdown-images/image-20200916225627910.png)

![image-20200916225634072](markdown-images/image-20200916225634072.png)

```python
result = pd.merge(df1, df2, left_on='학번', right_inex=True, how='inner')
display(result)
```

![image-20200916225654051](markdown-images/image-20200916225654051.png)