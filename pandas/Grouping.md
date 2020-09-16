# Grouping

> 주어진 `DataFrame`에 대하여 한개 이상의  `column`을 기준으로 `DataFrame` 자체 또는 `column` 을 grouping 또는 분류할 수 있다. `groupby` 라는 keyword를 사용한다.

다음의 예제를 고려하자.

```python
import numpy as np
import pandas as pd

my_dict = {'학과' : ['컴퓨터', '체육교육과', '컴퓨터', '체육교육과', '컴퓨터'],
           '학년' : [1, 2, 3, 2, 3],
           '이름' : ['홍길동', '김연아', '최길동', '아이유', '신사임당'],
           '학점' : [1.5, 4.4, 3.7, 4.5, 3.8]}
 
df = pd.DataFrame(my_dict)

display(df)
```

![image-20200915165356906](markdown-images/image-20200915165356906.png)



## Series의 Grouping

> `DataFrame`의 하나의 `column`을 grouping 하는 개념이다.

* `groupby` : grouping을 위한 keyword

```python
dept = df['학점'].groupby('학과') # 학과를 기준으로 학점을 grouping한다.
print(dept)   # <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001415A6EF7C8>

#  학과를 기준으로 학점을 분류를 해놨기 때문에 값이 나오지 않는다.
```



* `get_group ` : grouping 된것중에 원하는 group을 가져올 수 있다.

```python
print(dept.get_group['컴퓨터'])
# 0    1.5
# 2    3.7
# 4    3.8
# Name: 학점, dtype: float64

# Series를 grouping했으므로 Series로 출력된다.
```



* `size` , `mean` : 모든 group들의 개수와 평균값을 한번에 확인 가능하다.

```python
print(dept.size())
# 학과
# 체육교육과    2
# 컴퓨터      3
# Name: 학점, dtype: int64

print(dept.mean())
# 학과
# 체육교육과    4.45
# 컴퓨터      3.00
# Name: 학점, dtype: float64
```



## Series의 2단계 Grouping

> 기준 `column`이 하나가 아닌 경우를 사용할 수 있다. 기준 2개를 사용를 한 경우를 알아본다.

* `groupby` : 기준이 되는 `column`들을 `list`형태로 넣어준다.

```python
dept_rate = df['학점'].groupby([df['학과'],df['학년']])

print(dept_rate.size())
# 학과     학년
# 체육교육과  2     2
# 컴퓨터    1     1
#        3     2
# Name: 학점, dtype: int64

print(dept_rate.mean())
# 학과     학년
# 체육교육과  2     4.45
# 컴퓨터    1     1.50
#        3     3.75
# Name: 학점, dtype: float64

# Series와 DataFrame의 index와 column에 multi index를 지원해주는것을 알 수 있다.
```

* `unstack` : 최하위 index를 column으로 설정해 `DataFrame`으로 만들어 준다. 

```python
dept_rate = df['학점'].groupby([df['학과'],df['학년']]) # 최하위 column : '학년'
display(dept_rate.size().unstack())
```

![image-20200915172620615](markdown-images/image-20200915172620615.png)

```python
display(dept_rate.mean().unstack())
```

![image-20200915172651187](markdown-images/image-20200915172651187.png)



## DataFrame의 Grouping

> `Series` 뿐만 아니라 `DataFrame` 또한 grouping 가능하다.

* `groupby` : `Series`에 사용할 때와 달리 `DataFrame` 변수명을 포함해 입력할 필요없다.

```python
df_group_dept = df.groupby(df['학과'])
print(df_group_dept) # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001415A6EF488>
# Series와 달리 DataFrame으로 찍힌다.

display(df_group_dept.get_group('컴퓨터')) # DataFrame
```

![image-20200915173306059](markdown-images/image-20200915173306059.png)

```python
display(df_group_dept.mean())
```

![image-20200915173823843](markdown-images/image-20200915173823843.png)



## DataFrame의 2단계 Grouping

> 기준 `column`이 하나가 아닌 경우를 사용할 수 있다. 기준 2개를 사용를 한 경우를 알아본다.

* `groupby` : `Series`와 마찬가지로 기준이 되는 `column`들을 `list`형태로 넣어준다.

```python
df_dept_year = df.groupby(['학과','학년'])
display(df_dept_year.mean())  # multi index를 사용한다.
```

![image-20200915174230667](markdown-images/image-20200915174230667.png)

* `unstack` :최하위 index를  `DataFrame`의 column으로 설정한다. 

```python
display(df_dept_year.mean().unstack())
```

![image-20200915174436651](markdown-images/image-20200915174436651.png)



## Grouping의 반복 처리

> grouping 된 것들을 `for문`을 사용해 처리할 수 있다.  grouping 처리된 것들은 `tuple` 형태로 (기준, Series(or DataFrame)) 으로 구성되어 있다.

![image-20200916110406205](markdown-images/image-20200916110406205.png)

```python
for (dept, group) in df.groupby(['학과']):
    print(dept)
    display(group)
```

![image-20200916110528245](markdown-images/image-20200916110528245.png)

```python
for ((dept,year), group) in df.groupby(['학과','학년']):
    print(dept)
    print(year)
    display(group)
```

![image-20200916110704858](markdown-images/image-20200916110704858.png)



  