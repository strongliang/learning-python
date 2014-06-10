import random

def swap(list, p, q):
    list[p], list[q] = list[q], list[p]
    
def qs(a):
    if not a: return []
    if len(a)<=2:
        if a[0]>a[-1]: 
            swap(a, 0, 1)
        return a
    else:
        piv_idx = random.randrange(len(a)) # does not include the last elem, just like range
        piv = a.pop(piv_idx)
        lt = [e for e in a if e <= piv]
        gt = [e for e in a if e > piv]
        return qs(lt)+[piv]+qs(gt)
        
        
a = [random.randrange(10) for i in range(5)]
#a = [1, 2, 1, 3, 4]
print a
a_check = a[:]

a = qs(a)
print a

a_check.sort()

#print a
print a == a_check
        