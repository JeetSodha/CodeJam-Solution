def Caculate(t,res,Pr):
    if Pr != '' and t != '':
        if int(Pr) > int(t[0]):
            for i in range(int(Pr)-int(t[0])):
                res = res + ')'
    if t == '':
        for i in range(int(Pr)):
            res = res + ')'
        return res
    if int(t[0]) == 0:
        return Caculate(t[1:],res + t[0],t[0])
    if int(t[0]) == 1:
        if Pr != '':
            if int(Pr) == 0:
                res = res + '(' + t[0]
            else:
                res = res + t[0]
        else:
            res = res + '(' + t[0]
        return Caculate(t[1:],res,t[0])
    if int(t[0]) > 1:
        if Pr != '':
            for i in range(int(t[0]) - int(Pr)):
                res = res + '('
            res = res + t[0]
        else:
            for i in range(int(t[0])):
                res = res + '('
            res = res + t[0]
        return Caculate(t[1:],res,t[0])
t = int(input())
for m in range(0,t):
    k = input()
    print('Case #{}: {}'.format(m + 1,Caculate(k,'','')))