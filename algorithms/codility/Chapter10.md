# Chapter 10. 소수 및 합성수

* 소수 : 1보다 큰 자연수 중 약수의 개수가 정확히 2개 (1, 자기자신)인 수를 말한다.
* 합성수 : 약수의 개수가 2개 이상인 자연수



## 1. 약수의 개수 세기

n이 주어졌다고 하자. 가장 쉬운 접근 방법은 1에서 부터 n까지 iteration 하면서 각각이 약수인지 체크하는 방법이다.  즉, 다음 방법과 같다.

```python
result = 0
for i in range(n+1):
    if n%i == 0:
        result += 1
```

그러나 이 방법의 시간 복잡도는 O(n)이다.

이를 개선하기 위해 간단한 방법은 **symmetric** **divisor**를 찾는것이다. 즉 a가 n의 약수라면 n/a 역시 약수가 된다. 이중 작은 약수의 최댓값은 `sqrt(n)`이 된다. 그러므로 1부터 `sqrt(n)` 까지의 iteration만이 필요하다.

```python
def divisors(n):
	i = 1
    result = 0
    while i*i < n:
        if n%i == 0:
            result += 2
        i += 1
    if i*i == n:
        result += 1
    return result
```

시간 복잡도는 O(`sqrt`(n)) 이다.



## 2. 소수 판별법

n이 주어졌을 때 소수인지 판별 하는 방법은 위의 약수의 개수를 세는 방법과 거의 비슷하다.

```python
def isprime(n):
    i = 2
    while i*i < n:
        if n%i ==0:
            return False
    	i += 1
	return True
```

위의 방법을 사용하면 1과 2도 쉽게 걸러진다.



## 3. Exercise

n 개의 동전이 일렬로 주어졌을 때 각 동전은 앞면이 보이도록 놓여져 있다.

이때, n명의 사람이 동전을 다음과 같은 방법으로 뒤집는다.

 `사람 i 는 i의 배수들을 가진 모든 동전을 뒤집는다. 즉 i, 2i, 3i,.... `

결과 값은  뒷면을 보이는 모든 동전의 개수를 세는것이다.

```python
def coins(n):
    result = 0
    coin = [0]*(n+1)
    for i in range(1, n+1):
        k = i
        while k <= n :
            coin[k] = (coin[k] + 1) % 2
            k += i
```



