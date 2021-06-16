# 예외 처리

> 프로그램 코드는 이상이 없지만 실행 중에 불가피하게 발생하는 문제를 **예외(Exception)** 라고 한다. 이번 페이지에서는 처리하는 방법에 대해서 알아본다. 



* 심각한 에러 발생시 프로그램이 종료되어 이후의 명령이 무시되 제어권을 잃어버리는 경우가 있다. 
* 프로그램이 다운되어 버리면 손쓸 방법이 없기 때문에 최소한 어떤 문제가 있는지 친절히 알려 주기라도 해야 한다.

* 프로그램이 아무리 정교해도 예외는 발생할 수 밖에 없다.
* 예외를 막을 근본적인 방법이 없으니 어떡하든 모든 예외를 처리하는 수밖에 없다.



## 예외 처리

> 기본 예외 처리 구문을 알아본다.

* 예외 처리 구문 형식

  ```python
  try:
      실행할 명령
  except 예외 as 변수:
      오류 처리문
  else:
      예외가 발생하지 않을 때의 처리
  ```

  * 예외를 처리 구문이 예외 상황을 해결해 주지는 않지만 예외를 인식하고 처리 할 기회를 제공한다는 데 의미가 있다.



* 예제 1 : try ~ except ~ else ~

  ```python
  try:
      a = int('89점')
      print(a)
  except:
      print('예외가 발생했습니다.')
  else:
      print('예외 없이 잘 돌아갑니다.')
  print('작업 완료')
  
  # 예외가 발생했습니다.
  # 작업 완료
  ```

  * `try` 블록을 실행하고 예외가 발생하면 `except`구문을 실행한다.
  * `try` 블록을 실행하고 예외가 없으면 `else` 구문을 실행한다.

* 예제 2 : while ~ try ~ except ~

  ```python
  while True:
      str = input('점수를 입력하세요 : ')
      try:
          score = int(str)
          print('입력한 점수 :', score)
          break
      except:
          print('점수 형식이 잘못되었습니다.')
  print('작업완료')
  
  # 점수를 입력하세요 : 99점
  # 점수 형식이 잘못되었습니다.
  
  # 점수를 입력하세요 : 99 point
  # 점수 형식이 잘못되었습니다.
  
  # 점수를 입력하세요 : 99
  # 입력한 점수 : 99
  # 작업완료
  ```



* [백준 예제](https://www.acmicpc.net/problem/10951)

  ```
  문제
  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
  
  입력
  입력은 여러 개의 테스트 케이스로 이루어져 있다.
  
  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
  ```

  ```python
  import sys
  
  while True:
      try :
          a, b = map(int, sys.stdin.readline().split())
          print(a+b)
      except:
          break
  ```



## 예외의 종류

> 파이썬은 자주 발생하는 예외가 고유한 이름으로 붙여져 있다.



* 다음 예외들이 빈번히 발생한다.

| 예외              | 설명                                                 |
| ----------------- | ---------------------------------------------------- |
| NameError         | 초기화하지 않은 변수를 사용할 때 발생한다.           |
| ValueError        | 타입은 맞지만 값의 형식이 잘못되었다.                |
| ZeroDivisionError | 0으로 나누었다.                                      |
| IndexError        | 첨자가 범위를 벗어났다.                              |
| TypeError         | 타입이 맞지 않다. ex) 숫자 입력에 문자열 입력한 경우 |



* 예외가 여러 개 발생할 수 있는 경우

    * `IndexError`

        ```python
        str = '89'
        try:
            score = int(str)
            print(score)
            a = str[5]
        except ValueError:
            print('점수의 형식이 잘못되었습니다.')
        except IndexError:
            print('index 범위를 벗어났습니다.')
        print('작업완료')

        # 89
        # index 범위를 벗어났습니다.
        # 작업완료
        ```
        
    * `ValueError`

        ```python
        str = '89점'
        try:
            score = int(str)
            print(score)
            a = str[5]
        except ValueError:
            print('점수의 형식이 잘못되었습니다.')
        except IndexError:
            print('index 범위를 벗어났습니다.')
        print('작업완료')
        
        # 점수의 형식이 잘못되었습니다.
        # 작업완료
        ```

    

* 예외 여러개 한번에 처리

  ```python
  str = '89점'
  try:
      score = int(str)
      print(score)
      a = str[5]
  except (ValueError, IndexError):
      print('점수의 형식 또는 index 범위가 잘못되었습니다.')
  print('작업완료')
  
  # 점수의 형식 또는 index 범위가 잘못되었습니다.
  # 작업완료
  ```



* `as 키워드` : 예외 객체를 변수로 받으면 이 객체를 통해 에러 메세지를 얻을 수 있다.

  ```PYTHON
  str = '89점'
  try:
      score = int(str)
      print(score)
      a = str[5]
  except ValueError as e:
      print(e)
  except IndexError as e:
      print(e)
  print('작업완료')
  
  # invalid literal for int() with base 10: '89점'
  # 작업완료
  ```





## raise

> `raise` 명령은 고의적으로 예외를 발생시킨다.



* raise 뒤에 발생 될 예외의 이름을 적어 사용할 수 있다.

  ```python
  def calcsum(n):
      if n < 0:
          raise ValueError
      s = 0
      for i in range(n+1):
          s = s + i
      return s
  
  
  try:
      print('~10 =', calcsum(10))
      print('~-5 =', calcsum(-5))
  except ValueError:
      print('입력값이 잘못되었습니다.')
      
  # ~10 = 55
  # 입력값이 잘못되었습니다.
  ```

  

## finally

> finally 블록은 예외 발생 여부와 상관없이 반드시 실행 할 명령을 지정한다. 



* 예시 : 네트워크 접속한 후 통신을 수행하고 다 완료하면 접속을 끊는 것이 정상적인 순서이다.  

  →  통신 수행 중 예외가 발생해서 해제하지 못하면 네트워크를 계속 연결된 상태로 남아있다.

  → 이럴 때는 finally 블록에 작성에 두면 연결이 끊어짐을 보장할 수 있다.
  
  * 예제 코드
  
      ```python
      try:
          print('네트워크 접속')
          a = 2 / 0
        print('네트워크 통신 수행')
      finally:
          print('접속해제')
      print('작업 완료')
  
      ```
    
  * 결과
  
      ```python
      네트워크 접속
      접속해제
    Traceback (most recent call last):
        File "C:/Users/User/Desktop/GIT/TIL/algorithms/boj/tmp.py", line 3, in <module>
          a = 2 / 0
      ZeroDivisionError: division by zero
  
    Process finished with exit code 1
    ```
  
  

## assert

> 현재 상태가 맞는지 확인하는 기능을 한다. `점검할 조건`과 `조건이 거짓일 때 보여 줄 메세지`를 지정한다.



* 기본 구문 형식

  ```python
  assert 조건, 메세지
  ```

  * 조건을 점검하고 참이면 현재 상태가 정상적이라 판단 해 아무 일도 하지 않는다.
  * 거짓이면 AssertionError 예외를 발생시키고 프로그램을 즉시 중지하며 메세지를 보여 준다. (메세지는 생략 가능하다.)

  

* 예제

  ```python
  score = 128
  assert score <= 100, '점수는 100 이하여야 합니다.'
  print(score)
  
  # Traceback (most recent call last):
  #   File "C:/Users/User/Desktop/GIT/TIL/algorithms/boj/tmp.py", line 2, in <module>
  #     assert score <= 100, '점수는 100 이하여야 합니다.'
  # AssertionError: 점수는 100 이하여야 합니다.
  
  # Process finished with exit code 1
  ```

  * 개발자는 이 예외 처리 메세지를 보고 특정 변수에 잘못된 값이 들어갔는지 즉시 확인하고 해결할 수 있다.

  

* assert는 `이 조건이 맞는지 지금 당장 확인하라.` 를 뜻한다.



* 사용시 속도가 느려지는 문제가 있어 해석기를 실해할 때 -O 옵션을 주면 assert 문장을 모두 무시한다. `디버깅때 확인용으로만 사용하자.`

  ```bash
  $ python -O tmp.py
  128
  ```

  
