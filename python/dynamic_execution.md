# 동적 코드 실행

> 동적 코드 실행 방법에 대해서 알아본다.





## eval

> 프로그램이 자신을 스스로 만들어 낼 수 있고 사용자가 입력한 임의의 코드를 실행하는 것이 가능하다.



* `eval` 함수는 문자열 형태로 된 Python 표현식을 평가해 그 결과를 리턴한다.

* 이 함수를 사용해 실시간으로 코드를 만들어 실행할 수 있다.

    * 예제 1

        ```python
        result = eval("2+3*4")
        print(result)
        # 14
    a = 2
        print(eval('a+3'))
        
        # 5
        
        city = eval("['seoul', 'osan', 'suwon']")
        print(type(city))
        
        # <class 'list'>
        
        for c in city:
            print(c, end = ', ')
        
        # seoul, osan, suwon,
        ```
        
    * 예제 2

        ```python
        import math
        
        while True:
            try:
                expr = input('수식을 입력하세요(끝낼 때 0) : ')
                if expr == '0':
                    break
                print(eval(expr))
            except:
                print('수식이 잘못되었습니다.')
        
        수식을 입력하세요(끝낼 때 0) : 24
        # 24
        수식을 입력하세요(끝낼 때 0) : 365*24
        # 8760
        수식을 입력하세요(끝낼 때 0) : ㅍ
        # 수식이 잘못되었습니다.
        수식을 입력하세요(끝낼 때 0) : math.sqrt(2)
        # 1.4142135623730951
        수식을 입력하세요(끝낼 때 0) : 0        
        ```





## repr

> `str`과 유사하지만 결과가 표현식이라는 면에서 형식성이 더 엄격하고 객체로부터 문자열 표현식을 생성한다.



* 예제

  ```python
  print(str(1234), end=', ')
  print(str(3.14), end=', ')
  print(str(['seoul', 'osan', 'suwon']), end=', ')
  print(str('korea'))
  # 1234, 3.14, ['seoul', 'osan', 'suwon'], korea
  
  print(repr(1234), end=', ')
  print(repr(3.14), end=', ')
  print(repr(['seoul', 'osan', 'suwon']), end=', ')
  print(repr('korea'))
  # 1234, 3.14, ['seoul', 'osan', 'suwon'], 'korea'
  ```

  * 문자열에 대한 결과가 다르다.
  * `str` 함수는 사람이 읽기 쉽게 객체의 내용을 보여 주는것이 목적이기 때문에 사람이 쉽게 읽을 수 있게 보여준다.
  * `repr` 함수는 사람을 위한 문자열이 아닌 해석기를 위한 표현식을 만들어 내며 이 표현식으로 객체를 다시 만들 수 있다.

* 명령행에서 실행

  ```python
  >>> str('korea')
  Out[2]: 'korea'
  >>> repr('korea')
  Out[3]: "'korea'"
  ```

* `eval` 함수 사용해서 살펴보기

  ```python
  intexp = repr(1234)
  intvalue = eval(intexp)
  print(intvalue)
  
  strexp = repr('korea')
  strvalue = eval(strexp)
  print(strexp)
  ```

  



## exec

> 변수 정의, 반복문, if문 등 여러가지 코드안에 코드를 가능하게 해준다.



예를 들어, 다음의 코드는 error가 난다.

```python
eval('value=3')
print(value)
```

* `eval`의 경우 외부 변수를 참고만 할 뿐 직접 변수를 만들지 못한다. `eval`은 평가만 할 뿐 코드를 실행하지는 않는다.



* `exec`의 경우 파이썬 코드를 직접 실행한다.

* 예제 1

  ```python
  exec('value=3')
  print(value)
  # 3
  
  exec("for i in range(5):print(i, end=', ')")
  # 0, 1, 2, 3, 4,
  ```

* 예제  2 : 들여쓰기 할 때 조심해야 한다. 파이썬 규칙에 맞게 들여쓰기를 지켜야 한다.

  ```python
  for n in range(10):
      exec("""
  for i in range(5):
      print(i, end=', ')
  print()
      """)
      
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  # 0, 1, 2, 3, 4, 
  ```

  

