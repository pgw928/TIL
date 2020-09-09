## Series

> **동일한 데이터 타입**의 복수개의 성분으로 구성되는 자료구조이다.
* 1차원 구조이다.
* `Numpy`의 `ndarray` 기반으로 되어있다.

  


## Series 기초

> `Pandas`의 `Series`를  이용해 만들 수 있다.

```python
import numpy as np
import pandas as pd # pd로 줄여서 사용한다.

s = pd.Series([-1,4, 5, 99], dtype=float64)
print(s)
# 0    -1
# 1     4
# 2     5
# 3    99
# dtype: float64
print(s.values)    # [-1.  4.  5. 99.]
print(s.index)     # RangeIndex(start=0, stop=4, step=1)
print(s.dtype)     # float64
```

* `print(s)` : 모든 정보가 나온다. `index`, `values`, `dtype` 을 알려주며 `name`명시하면 `name`도 함께 출력된다.
* `print(s.values)` : `Series`의 `ndarray`로 된 `values`가 출력된다.
* `print(s.index)` : `Series`의 `index`값들이 출력된다. 기본 index에 대해서는 실제값들이 나오지는 않고 위와 같이 출력된다.
* `print(s.dtype) ` : `Series`의 `dtype`, 즉, `values`의 dtype이 나온다.



## index

> `Series` 생성 시 `index` option을 별도로 지정할 수 있다.  지정시 list로 표현된다.  **중복**도 가능하다.

```python
s = pd.Series([1, -8, 5, 10], dtype=np.float64, index=['b','a','c','d'] )
print(s)
# b     1.0
# a    -8.0
# c     5.0
# d    10.0
# dtype: float64
print(s['c'])   # 5.0
print(s[2])     # 5.0
```

* `print(s)` :  숫자형 `index`가 지정한 `index` 로 출력된다.
* `print(s['c'])` : 이와 같이 `indexing`이 가능하다.
* `print(s[2])` : 여전히 숫자형 `index` 를 사용할 수 있다.



## Slicing

> 숫자 index를 가지고 다른 인덱스가 있는 자료형과 같이 `slicing` 가능하고 **문자 index**를 이용해서도 가능하다.

 ```python
print(s[1:3])
# a   -8.0
# c    5.0
# dtype: float64
print(s['a':'c'])
# a   -8.0
# c    5.0
# dtype: float64
 ```

* 문자 index는 숫자 index와 다르게 `stop`을 포함해서 출력한다.

### (참고)

**`Series`는 `ndarray` 기반이기 때문에 `Boolean indexing`, `Fancy indexing`, 그 밖의  `numpy` 함수나 method를 그대로 사용할 수 있다. **



## dictionary를 이용한 Series

> python의 `dictionary`를 이용해 `Series`를 만들어 본다.

* dictionary의  `key`는 Series의 `index`로 마찬가지로 `value`는 Series의 `value`로 대응된다.

```python
import pandas as pd
import numpy as np

my_dict = {"떡볶이":1500, "순대":3500, "튀김":2500}
s = pd.Series(my_dict)
print(s)
# 떡볶이    1500
# 순대     3500
# 튀김     2500
# dtype: int64
```

* Series에는 `name` 속성을 추가할수 있다. `index`와 `Series` 두가지에 만들어 줄 수 있다.

```python
s.name = "분식집"
s.index.name = '메뉴'
print(s)
# 메뉴
# 떡볶이    1500
# 순대     3500
# 튀김     2500
# Name: 분식집, dtype: int64
```



