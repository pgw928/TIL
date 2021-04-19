import sys
sys.stdin = open('section6/input.txt', 'rt')
n = int(input())

s = ''
def to_binary(k):
    global s
    if k==1:
        s = '1' + s
        return
    
    if k%2==1:
        s = '1' + s
        to_binary(k//2)
    elif k%2 == 0:
        s = '0' + s
        to_binary(k//2)

to_binary(n)
print(s)  
