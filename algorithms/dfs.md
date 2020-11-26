# Depth-First Search (깊이 우선 탐색)

> 대표적인 그래프 탐색 알고리즘인 깊이 우선 탐색에 대해서 알아본다.

![image-20201124175610412](markdown-images/image-20201124175610412.png)



## DFS 구현 방법

* 위의 그래프를 DBFS 방식으로 탐색해보면 위의 빨간색 방향과 같이

A-B-D-E-F-C-G-H-I-J 가 된다. (BFS 알고리즘에서 최종 출력값이다.)

*  위의 그래프를 `dictionary`와 `list` 자료 구조를 활용하여 주로 나타낼 수 있다.

| key  | valuess |      |      |      |      |
| ---- | ------- | ---- | ---- | ---- | ---- |
| A    | B       | C    |      |      |      |
| B    | A       | D    |      |      |      |
| C    | A       | G    | H    | I    |      |
| D    | B       | E    | F    |      |      |
| E    | D       |      |      |      |      |
| F    | D       |      |      |      |      |
| G    | C       |      |      |      |      |
| H    | C       |      |      |      |      |
| I    | C       | J    |      |      |      |
| J    | I       |      |      |      |      |

  ```python
graph_list = {'A':(['B','C']),
              'B':(['A','D']),
              'C':(['A','G','H','I']),
              'D':(['B','E','F']),
              'E':(['D']),
              'F':(['D']),
              'G':(['C']),
              'H':(['C']),
              'I':(['C','J']),
              'J':(['I'])}
  ```

* 주로 `stack` 자료 구조를 사용한다.





## 반복을 통한 DFS 알고리즘 코드

> 반복문(iteration)을 이용해 DFS를 구현한다.

```python
from collections import deque 

def dfs(graph, start_node):

    visited= []
	need_visit = deque(start_node)
   
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited 
```

* `from collections import deque` : `list` 자료 구조를 사용해도 되지만 속도면에서 deque를 사용한다.

* `def dfs(graph_list, start_node)`  : `graph` 및 `start_node`(root node)를 input으로 받는다.
* `need_visit.extend(graph_list[node])` : 사실상 `visited` 를 고려하지 않고 `need_visit` 에 원소를 추가한다.



### 결과

```python
start_node = 'A'
print(dfs(graph_list, start_node))
# ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
```

* 이 경우 우리가 원하는 좌측 먼저 가는게 아니라 우측을 먼저 순회하게 된다.



## 재귀(Recursion)를 활용한 DFS 알고리즘 코드

> 재귀(Recursion)을 이용해 DFS를 구현한다.

```python
def recursive_dfs(graph, start_node, visited=[]):

    visited.append(start_node)
	
    for node in graph[start_node]:
    	if node not in visited:
            recursive_dfs(graph, node, visited)

    return visited
```

### 결과

```python
start_node = 'A'
print(recursive_dfs(graph_list, start_node))
# ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J']
```

