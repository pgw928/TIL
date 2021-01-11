import sys
input  = sys.stdin.readline

a = int(input())
m = 1
cnt = 0
list = []
sort_list = []
copy_list=[]
stack_list = ""

for i in range(a): list.append(int(input()))
for item in list:

    for i in range(m,item+1):
        stack_list += "+\n"
        sort_list.append(i)
        cnt+=1
    m = cnt+1
    stack_list +="-\n"
    copy_list.append(sort_list.pop(-1))
if list == copy_list:
    print(stack_list,end='')
else:
    print("NO")