## 컬렉션 관리 함수 및 람다 함수

> 컬렉션 관리 함수 와 람다 함수를 정리한다.

## 1. enumerate

> index와 list 요소를 둘 다 읽어야 할 때 편리하다.



* 기본 사용법

    ```python
    score = [88, 95, 70, 100, 99]
    for no, s in enumerate(score):
        print('{}번 학생의 성적 : {}'.format(no, s))
    
    # 0번 학생의 성적 : 88
    # 1번 학생의 성적 : 95
    # 2번 학생의 성적 : 70
    # 3번 학생의 성적 : 100
    # 4번 학생의 성적 : 99
    ```

    

* 시작 index 바꾸기
    ```python
    score = [88, 95, 70, 100, 99]
    for no, s in enumerate(score,1):
        print('{}번 학생의 성적 : {}'.format(no, s))
    # 1번 학생의 성적 : 88
    # 2번 학생의 성적 : 95
    # 3번 학생의 성적 : 70
    # 4번 학생의 성적 : 100
    # 5번 학생의 성적 : 99
    ```





## 2. zip

> 두개 이상의 iterable을 묶어 줄 때 편리하다.



* 기본 사용법

    ```python
    yoil = ['월', '화', '수', '목', '금', '토', '일']
    food = ['갈비탕', '순대국', '칼국수', '삼겹살']

    menu = zip(yoil,food)
    for y, f in menu:
        print(y,f)
    # 월 갈비탕
    # 화 순대국
    # 수 칼국수
    # 목 삼겹살

    d = dict(zip(yoil, food))
    print(d)
    {'월': '갈비탕', '화': '순대국', '수': '칼국수', '목': '삼겹살'}
    ```



## 3. any, all

> `any`의 경우 하나라도 `True`이면 `True`를 , `all`의 경우 모두가 `True`이면 `True`를 return 한다.



* 기본 사용법

    ```python
    adult = [True, True, False, False]
    print(any(adult)) # True
print(all(adult)) # False
    
    adult = [1, 1, 0, 1]
    print(any(adult)) # True
    print(all(adult)) # False
    ```



## 4. filter

> filter 보다 `list comprehension`을 사용하는게 좋지만 알아본다.



* 기본 사용법

    ```python
    score = [45, 89, 72, 53, 94]
    for s in filter(lambda s: s<60, score):
        print(s)
    # 45
    # 53

    l_filter = list(filter(lambda s: s<60, score))
    print(l_filter)
    # [45, 53]
    ```



## 5. map

> 모든 요소에 대해서 변환 함수를 호출 해 새로 구성된 리스트를 생성한다.



* 기본 사용법

    ```python
    for s in map(lambda s: s/2 ,score):
        print(s)  
    # 22.5
    # 44.5
    # 36.0
    # 26.5
    # 47.0 

    print(list(map(lambda s: s/2 ,score)))
    # [22.5, 44.5, 36.0, 26.5, 47.0]
    ```

* iterable이 두개 이상일 때

  ```python
  def total(a, b):
      return a + b
  
  for n in map(total, [1, 2, 3, 4], [10, 20, 30, 40]):
      print(n, sep=', ')
  # 11, 22, 33, 44, 
  ```

  