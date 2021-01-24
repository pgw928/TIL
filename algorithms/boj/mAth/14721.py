import sys

input = sys.stdin.readline

n = int(input())

X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# a * sum(X)*sum(X) + b* n*sum(X) - sum(Y)*sum(X) = 0
# a * sum([ i**2 for i in X]) + b * sum(X)- sum([x*y for x,y in zip(X,Y)])

a = (sum(Y)*sum(X)- n*sum([x*y for x,y in zip(X,Y)]))/(  sum(X)*sum(X) - n* sum([ i**2 for i in X])   )
b =  (sum(Y)*sum(X) - a * sum(X)*sum(X))/(n*sum(X))

# a * sum(X)*sum(X) + b* n*sum(X) - sum(Y)*sum(X) = 0
print(round(a), round(b))

