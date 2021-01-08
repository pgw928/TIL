import sys

input = sys.stdin.readline


R, C = map(int, input().split())

graph = [list(input().strip())  for _ in range(R)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
