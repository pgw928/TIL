# 변수의 범위
> local variable와 global variable에 대해서 알아 본다.



## local variable

> 함수 내부에서 선언된 변수를 지역 변수(local variable)이라고 한다.



* 밑에서 `sum` 이라는 지역 변수를 사용한다.

    ```python
    def calsum(n):
        sum = 0
        for num in range(n+1):
            sum += num
        return sum
    ```

* 지역 변수의 사용 범위를 함수 내부로 제한하는 이유는 이름 충돌을 피하고 함수 동작에 필요한 모든 것을 내부에 포함시켜 **독립성**을 향상시키기 위함이다.

  ```python
  def kim():
      tmp = '김과장 함수'
      print(tmp)
      
  def lee():
      tmp = 2**10
      return tmp
  
  def park(a):
      tmp = a*2
      print(6)
      
  kim()        # 김과장의 함수
  print(lee()) # 1024
  park(6)		 # 12
  
  # tmp는 모두 이름만 같고 다른 변수이다.
  ```





## global variable

> 함수 바깥에서 선언하는 변수를 전역 변수(global variable)라고 한다.



* 밑의 코드에서 `salerate`가 전역 변수이다.

  ```python
  salerate = 0.9
  
  def kim():
      print('오늘의 할인율 :', salerate)
  
  def lee():
      price = 1000
      print('가격 :', price*salerate)
      
  kim()     # 오늘의 할인율 : 0.9
  
  salerate = 1.1
  lee()     # 가격 : 1100.0
  ```



* 주의 할 점 : 지역, 전역끼리 이름이 같아도 상관은 없지만 함수 내부에서 `지역 변수가 우선이라는 규칙`을 적용한다.

  ```python
  price = 1000
  
  def sale():
      price = 500
      print(price)
  
  sale()        # 500   : 지역변수 값을 출력한다.
  print(price)  # 1000  : 전역변수 값이 변하지 않는다.
  ```



* 새로운 지역 변수가 아니라 전역 변수의 값을 변경하고자 하는 경우는 `global` 명령어를 사용한다.

  ```python
  price = 1000
  
  def sale():
      global price
      price = 500
      print(price)
  
  sale()         # 500 
  print(price)   # 500 : 함수 내부의 price가 global variable로 바뀌어 price 값을 바꿔준다.
  ```



* 주의할 점 : 원칙적으로 전역 변수를 자재하는 것이 좋고 정 필요하면 `g_price` 식으로 이름에 전역임을 표시해 충돌을 사전에 방지하는 것이 합리적이다.