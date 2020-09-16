# DataFrame의 결합(merge)(1)

>두 DataFrame을 Database 결합(join)하기 위해서는 두개의 DataFrame과 기준(`on`), 방법(`how`) 옵션이 들어간다. 다음의 예제를 통해 여러가지 방법에 대해서 알아본다.

![image-20200915024044786](markdown-images/image-20200915024044786.png)

```python
import numpy as np
import pandas as pd 
data1 = {'학번' : [1, 2, 3, 4],
        '이름' : ['이지안','박동훈','이순신','강감찬'],
        '학년' : [2, 4, 1, 3]}


data2 = {'학번' : [1, 2, 4 ,5],
         '학과' : ['CS','MATH','MATH', 'CS'],
         '학점' : [3.4, 2.9, 4.5, 1.2]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
display(df1)
display(df2)
```

![image-20200915022613912](markdown-images/image-20200915022613912.png)

![image-20200915022626320](markdown-images/image-20200915022626320.png)



## full outer join

> Outer join은 두 `DataFrame`의 합집합으로 생각할 수 있다. option에는 `how='outer'` 가 입력된다.

```python
result = pd.merge(df1, df2, on ='학번', how='outer')
display(result)
# 학번을 기준으로 합집합 연산을 합니다.
```

![image-20200916165858323](markdown-images/image-20200916165858323.png)

## Full left join

> Left join은 두 `DataFrame` 을 `df1` , `df2` 라 하면 `df1`에 `df2-df1` 을 합집합 해준다고 생각 할 수 있다.

```python
result1 = pd.merge(df1, df2, on='학번', how='left')
display(result1)
# 아래 display를 보면 df1에 (df2-df1) : 학과, 학점이 추가 되었다.
```

![image-20200916165832779](markdown-images/image-20200916165832779.png)

## Full right join

> Right join은  left join 과 마찬가지 역할로 `df1`, `df2` 순서만 변했다고 생각 할 수 있다. 대신 `df2`의 `column` 이 뒤에 붙는다.

```python
result2 = pd.merge(df1, df2, on='학번', how='right')
display(result2)
```

![image-20200916170343364](markdown-images/image-20200916170343364.png)

반대로 `df1` 과 `df2` 순서를 바꿔보면

```python
result3 = pd.merge(df2, df1, on='학번', how='right')
display(result3)
```

![image-20200916173630814](markdown-images/image-20200916173630814.png)

Full left join에서의  `column`  순서를 제외한 같은 결과물을 얻을 수 있다.

