# 가변 인수

> 함수를 작성할 때 가변 인수에 대해 다룬다.



## 위치 가변 인수

> 키워드를 사용하지 않는 가변 인수에 대해 알아본다.

* 위치 가변 인수는 임의 개수의 인수를 받는다. `*` 기호를 붙이면 여러 개의 인수가 올 수 있다. 이때 인수는 **tuple**로 묶여 전달 된다.

  ```python
  def intsum(*arg):
  
      s = 0
      for n in arg:
          s+=n
      return s
  
  print(intsum(2))         # 2
  print(intsum(2,3,4)) 	 # 9
  print(intsum(1,2,3,4,5)) # 15
  ```

  이때 가변 인수는 이후의 모든 인수를 전부 포함하기 때문에 마지막에 와야 한다.

  ```python
  intsum(a, *arg)   	 # 가능
  intsum(*arg, a)      # error
  intsum(*arg1, *arg2) # error
  ```



* 가변인자를 받는 대표적인 함수는 `print` 이다.

  ```python
  print('취업', '원해요.') # 취업 원해요.
  print(1,2,3,4) 		   # 1 2 3 4
  ```

  

## 키워드 가변 인수

> 키워드를 사용하는 가변 인수에 대해서 알아본다.



* 키워드 인수를 개변 개수로 전달할 때는 인수 목록에 `**` 를 붙인다. 여러 개의 키워드 인수를 전달하면 인수의 이름과 값의 쌍을 **dictionary** 로 만들어 전달한다.

  ```python
  def calcstep(**args):
  
      begin = args['begin']
      end = args['end']
      step = args['step']
  
      sum = 0
      for num in range(begin, end+1, step):
          sum += sum
      return sum
  
  print('3 ~ 5 =', calcstep(begin=3, end = 5, step = 1)) # 3 ~ 5 = 0
  print('3 ~ 5 =', calcstep(end = 5, begin=3, step = 1)) # 3 ~ 5 = 0
  ```





## 마치며

#### 위치 가변 인수와 키워드 가변 인수를 함께 사용할 수 있고 파이썬의 유연성이 잘 드러나는 부분이지만 너무 과도하면 인수 전달 과정이 헷갈려 어려워지는 단점이 있다.

