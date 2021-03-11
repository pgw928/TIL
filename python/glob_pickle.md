# glob 및 pickle

> 파일을 입맛대로 요리할 수 있는 방법들이다.



## glob

> 파일명을 리스트로 넣을 때 사용한다. 파일의 경로명을 이용해 원하는대로 사용가능하다.

```python
from glob import glob

print(glob('*.ipynb')) # 현재 폴더의 모든 .ipynb 를 list에 저장한다.
# ['base.ipynb', 'glob_pickle.ipynb', 'pandas 문자열 처리.ipynb']

print(glob('C:\\U*')) # C:\에서 이름이 U로 시작하는 폴더나 파일을 찾는다.
# ['C:\\Users', 'C:\\User_manual']
```



## pickle

> 조금 복잡한 자료를 파일에 쓰고 읽을 때 사용한다.



간단한 예제로 회원의 ID와 비밀번호를 파일에 저장하는 것을 생각한다.

```python
import pickle
users = {'kim':'3kid9', 'sun80':'3939948', 'ljm':'py90390'}

f = open('users', 'wb')
pickle.dump('users', f)
f.close()
```

* `users = {'kim':'3kid9', 'sun80':'3939948', 'ljm':'py90390'}` : 아이디와 비밀번호를 사전으로 만든다.
* `f = open('users', 'wb')` : users라는 파일을 새로 열어 f라는 이름을 붙인다. 이때 `wb`는 text가 아닌 **b**yte 형식으로 쓰겠다(**w**rite)는 뜻이다.
* `pickle.dump('users', f)` : 공사장에서 흙을 실어나르는 덤프 트럭이 뒤쪽 짐칸을 들어올려 흙을 와르르 쏟아내는 것과 같이 users라는 리스트를 파일 f에 기록한다.



```python
f = open('users', 'rb')
a = pickle.load(f)
print(a)   # {'kim': '3kid9', 'sun80': '3939948', 'ljm': 'py90390'}

f.close()
```

* `a = pickle.load(f)` : `'users'` 에 기록했던 리스트를 가져온다.

