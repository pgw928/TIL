# 이차원 이상의 리스트 복사

> 일반적인 복사로 이중 리스트 복사가 되지 않는다.  따라서 이차원 이상의 리스트 복사하는 방법에 대해서 알아본다. 





## 일반적인 방법을 사용했을때

> 일반 리스트를 복사할 때 주로 사용하는 방법은 `.copy()` 나 `[:]` 를 이용하는 방법이다.

```python
N =5
graph = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]
graph1 = graph[:]

for i in range(N):
    for j in range(N):
        if graph1[i][j]=='R':
            graph1[i][j]='G'
# 위에서 graph1의 'R' 부분을 'G'부분으로 모두 바꿨다.
            
print(graph)
# [['G', 'G', 'G', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'G', 'G'], ['B', 'B', 'G', 'G', 'G'], ['G', 'G', 'G', 'G', 'G']]

print(graph1)
# [['G', 'G', 'G', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'G', 'G'], ['B', 'B', 'G', 'G', 'G'], ['G', 'G', 'G', 'G', 'G']]

```

* 위의 코드 결과로 보면 `graph1` 만 값을 변경했을 뿐인데 원본인 `graph`에도 똑같이 영향을 주는것을 알 수 잇다.
* 이는 `.copy()`를 이용했을 때도 똑같은 현상이 발생한다.



## 해결 방법

> `copy module`의 `deepcopy`를 사용하면 쉽게 해결된다.

```python
N =5
graph = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]
graph1 = copy.deepcopy(graph)

for i in range(N):
    for j in range(N):
        if graph1[i][j]=='R':
            graph1[i][j]='G'
# 위에서 graph1의 'R' 부분을 'G'부분으로 모두 바꿨다.
            
print(graph)
# [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]

print(graph1)
# [['G', 'G', 'G', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'G', 'G'], ['B', 'B', 'G', 'G', 'G'], ['G', 'G', 'G', 'G', 'G']]

```

* `graph1`을 변경해도 원본 데이터 `graph`에는 영향이 없는것을 확인해 볼 수 있다.



## 출처

* [https://dojang.io/mod/page/view.php?id=2294] : 방법은 이곳에서
* [https://www.acmicpc.net/problem/10026] : graph data는 적록색약 문제 

