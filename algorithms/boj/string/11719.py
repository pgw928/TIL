i = 0
while i<100:
    try:
        s = input()
        if s[-2:]=='\n':
            print(s[:-2])
        else:
            print(s)
    except:
        break
    i += 1
