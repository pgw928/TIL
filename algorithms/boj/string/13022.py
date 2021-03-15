import sys
st = sys.stdin.readline().strip()
l = len(st)
idx, count = 0, 0
flag = False
w_c, o_c, l_c, f_c = 0, 0, 0, 0
for s in st:
    print(s, w_c, o_c, l_c, f_c)
    if s=='w':
        w_c += 1
        if l_c!=f_c or o_c!=l_c:
            flag = True
            break

    elif s=='o':
        o_c += 1
        if w_c < o_c:
            flag = True
            break

    elif s=='l':
        l_c += 1
        if o_c < l_c or w_c!=o_c:
            flag = True
            break

    elif s=='f':
        f_c += 1
        if l_c < f_c or o_c!=l_c:
            flag = True
            break

print(w_c, o_c, l_c, f_c)
if flag or w_c!=o_c or o_c!=l_c or l_c!=f_c:
    print(0)
else:
    print(1)