
a = list('abcd')

def perm(a):
    res = []
    
    if len(a) == 1:
        return a
        
    for i in range(len(a)):
        sub = a[:i] + a[i+1:]
        for p in perm(sub):
            res.append(a[i] + p)
    return res

res = perm(a)
print res
#print len(res)

    