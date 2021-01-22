# 여러가지 method

> class 관련 여러 method에 대해 정리한다.



## class method

> 인스턴스 method가 아닌 class method에 대해 알아본다. (`self` 를 사용하지 않는다.)



* 함수 위에 `@classmethod` 데코레이터를 붙이고 인수로 클래스를 의미하는 `cls` 인수를 받는다.

  ```python
  class Car:
  
      count = 0
      def __init__(self, name):
          self.name = name
          Car.count += 1
      @classmethod
      def outcount(cls):
          print(cls.count)
  
  pride = Car('프라이드')
  korando = Car('코란도')
  Car.outcount()  # 2
  ```

  * 최초 `Car`을 선언할 때 0으로 초기화하고 `__init__`에서 차를 한 대 생성할 때마다 1씩 증가한다.

  * `print(pride.count)` 를 입력해도 값은 `2`를 출력한다. 그러나 `Car.count`가 원칙이다.





## static method

>class에 포함되는 단순한 `유틸리티 method`이다. 특정 객체에 소속되지 않으므로 `self` 또는 `cls` 인수를 받지 않는다. 



* 함수 위에 `@staticmethod` 데코레이터를 붙인다.

  ```python
  class Car:
  
      @staticmethod
      def hello():
          print('오늘도 안전 운행 합시다.')
      count = 0
      def __init__(self, name):
          self.name = name
          Car.count += 1
      @classmethod
      def outcount(cls):
          print(cls.count)
  
  Car.hello()
  # 오늘도 안전 운행 합시다.
  ```

  * 클래스와 객체와 직접적인 연관이 없고 단순히 클래스에 소속되어 있을 뿐이다.
  * 객체가 전혀 없어도 호출 가능하며, 객체와 상관없는 일반적인 동작만 가능하다.





## operator method

> 연산자 메소드를 정의하면 객체에 대해서도 연산을 사용할 수 있다.  (예를 들어, `human1==human2` 와 같이)



* 연산자 종류
    | 연산자 |     메소드     | 우변일 때의 메소드 |
    | :----: | :------------: | :----------------: |
    |   ==   |    `__eq__`    |                    |
    |   !=   |    `__ne__`    |                    |
    |   <    |    `__it__`    |                    |
    |   >    |    `__gt__`    |                    |
    |   <=   |    `__le__`    |                    |
    |   >=   |    `__ge__`    |                    |
    |   +    |   `__add__`    |     `__radd__`     |
    |   -    |   `__sub__`    |     `__rsub__`     |
    |   *    |   `__mul__`    |     `__rmul__`     |
    |   /    |   `__div__`    |     `__rdiv__`     |
    |   /    | `__truediv__`  |   `__rtruediv__`   |
    |   //   | `__floordiv__` |  `__rfloordiv__`   |
    |   %    |   `__mod__`    |     `__rmod__`     |
    |   **   |   `__pow__`    |     `__rpow__`     |
    |   >>   |  `__lshift__`  |   `__rlshift__`    |
    |   <<   |  `__rshift__`  |    `__lshift__`    |



* 예제 : `__eq__` 메소드를 정의하면 `==` 연산으로 비교 가능하다.

  ```python
  class Human:
  
      def __init__(self, age, name):
          self.age = age
          self.name = name
      def __eq__(self, other):
          return self.age == other.age and self.name == other.name
  
  
  human1 = Human(29, '김상혁')
  human2 = Human(29, '김상형')
  human3 = Human(29, '김상혁')
  
  print(human1 == human2)     # False
  print(human1 == human3)		# True
  ```

  * 객체끼리 비교는 클래스별로 다르다.
  * huma1



## special method

> 특수 메소드는 특정한 구문에 객체가 사용되면 자동으로 호출되어 객체에 대해 원하는 작업을 수행한다. 



* speical method 종류

  |   method   | 설명                                        |
  | :--------: | ------------------------------------------- |
  | `__str__`  | str(객체) 형식으로 객체를 문자열화한다.     |
  | `__repr__` | repr(객체) 형식으로 객체의 표현식을 만든다. |
  | `__len__`  | len(객체) 형식으로 객체의 길이를 조사한다.  |

  

* `__str__` 예제 : 객체를 `print`로 출력하면 미리 지정해 둔 문자열로 보여준다.

  ```python
  class Human:
  
      def __init__(self, age, name):
          self.age = age
          self.name = name
      def __str__(self):
          return f'이름 {self.name}, 나이 {self.age}'
  
  
  human1 = Human(29, '김상혁')
  print(human1)
  # 이름 김상혁, 나이 29
  ```

  * `__str__`함수를 정의하지 않으면 `<__main__.Human object at 0x000001B1F96DCF08>` 과 같이 출력된다.



* `__repr__` 또한 같은 역할을 하지만 **공식적인(official)** **문자열**을 출력할 때 사용하고 `__str__`은 객체의 **비공식적인(informal)** **문자열**을 출력할 때 사용한다.

  `eval(repr(object))`를 사용하면 object를 얻을 수 있다.



* `__len__` 예제 : 객체에 대한 `len`을 정의할 수 있다.

  ```python
  class Human:
  
      def __init__(self, age, name):
          self.age = age
          self.name = name
      def __len__(self):
          return self.age
  
  
  human1 = Human(29, '김상혁')
  print(len(human1))
  # 29
  ```

  