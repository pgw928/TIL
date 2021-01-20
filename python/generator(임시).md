# generator

> 이터레이터를 직접 만들 때 사용하는 것으로 함수 내부에 yield 라는 키워드가 포함된 함수이다.

* 제네레이터 객체는 모든 값을 메모리에 올려두고 이용하는게 아니라 필요할 때마다 생성해서 반환하는 일을 한다.
* 이 때문에 메모리를 효율적으로 사용할 수 있다.



제너레이터와 이를 이용한 for 문

```python
my_generator = (i for i in range(1,4))

for n in my_generator:
    print(n)

type(my_generator)
```

: 반복자와 동일한 일을 하는 것처럼 보이지만 여기서 생성된 1, 2, 3을 미리 메모리에 만들어 두는게 아니라 `for `문에서 필요할 때맏 my_generator로 부터 받아오며 메모리에서 보관하지 않는다는 점이다. (lazy evaluation 이라 함)



yield

* yoeld문은 제너레이터를 만들 때 사용한다는 점에서 return문과 차이가 있다.
* 



제네레이터

* 실행될 때 함수의 몸체를 실행하는 것이 아니라, 함수가 가진 객체를 반환하는 일을 한다.
* 제네레이터는 한번 생성해서 반환한 객체를 보관하지 않기 때문에 이전의 코드를 실행한 후 추가한 코드를 실행하면 아무런 객체도 출력하지 않는다.

```python
def create_gen():
    alist = range(1,4)
    for x in alist:
        yield x

my_generator = create_gen()
print(my_generator) # <generator object create_gen at 0x0000029031074348>
for n in my_generator:
    print(n)
# 1
# 2
# 3
for n in my_generator: # my_generator에 아무것도 없게 된다.
    print(n)
    
```



## 정리

* 제네레이터는 메모리를 절약해 준다.
* 수행시간도 절약해 준다.