# docstring

> 모듈, 함수, 클래스 또는 메소드 정의의 첫 번째 명령문으로 발생하는 `문자열 리터럴`이다.



* 함수의 재활용성을 높이려면 자세한 함수 사용법, 인수의 의미, 주의 사항 등을 문서로 남겨야 한다.
* 별도의 문서나 주석을 사용할 수 있지만 공식적인 방법은 **docstring**을 작성하는 것이다.
* 한 줄일때는 단순 따옴표를 쓸 수 있지만 보통 긴 설명을 작성하기 때문에 **삼겹** **따옴표**를 활용한다.
* **docstring**을 읽을 때는 `help` 함수를 사용한다.

* 예시

    ```python
    def calcsum(n):
        '''1~n까지의 합계를 구해 리턴한다.'''
        sum = 0
        for i in range(n+1):
            sum += i
        return sum

    help(calcsum)
    ```

* 결과

    ```python
    Help on function calcsum in module __main__:

    calcsum(n)
        1~n까지의 합계를 구해 리턴한다.
    ```

* **docstring**만 읽으려면 `__doc__`를 사용한다.

    ```python
    print(calcsum.__doc__)
    # 1~n까지의 합계를 구해 리턴한다.
    ```



* 내장 함수

    ```python
    help(max)
    Help on built-in function max in module builtins:

    max(...)
        max(iterable, *[, default=obj, key=func]) -> value
        max(arg1, arg2, *args, *[, key=func]) -> value

        With a single iterable argument, return its biggest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more arguments, return the largest argument.
    ```



