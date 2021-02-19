#
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

def sol(m):
    '''
    시간의 최댓값과 최솟값을 설정하고
    최댓값과 최솟값의 중간값의 시간에서
    모두 입국이 가능하면 최댓값을 중간값으로,
    불가능 하면 최솟값을 중간값으로 교체해
    최종적으로 시간의 최댓값을 출력하는 방식의
    binary search로 코드를 작성했다.
    '''
    i = 1  # 가능한 시간의 최솟값
    M = m * arr[0]  # 가능한 시간의 최댓값
    if len(arr) == 1:
        return M
    while M - i >= 2:
        j = (i + M) // 2  # 중간값
        s = 0  # 심사 받은 인원의 수
        for a in arr:
            if s < m:  # 현재 m명 미만 검사했으면 계속 검사
                s += j // a
            else:  # 현재 m명 이상 검사 가능하면 그만
                break
        if s >= m:  # m명보다 더 검사했으면 시간의 최댓값 M을 중간값 j로 교체
            M = j
        else:  # m명보다 더 적게 검사했으면 시간의 최솟값 i를 중간값 j로 교체
            i = j
    return M

print(sol(m))