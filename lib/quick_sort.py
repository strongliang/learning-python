from decorator import *
def swap(list, p, q):
    list[p], list[q] = list[q], list[p]

@trace    
def qs(a, st, end, verbose=False):
    if st==end: return
    elif st==end-1: 
        if a[st]>a[end]: swap(a, st, end)
        
    else:
        lptr, rptr = st+1, end
        mid = (st+end)/2
        piv = a[mid]
        swap(a, st, mid)

        done = False
        while not done:
            while lptr<rptr and a[lptr]<piv: lptr += 1
            while lptr<=rptr and a[rptr]>=piv: rptr -= 1
            if verbose: print a, piv, [a[lptr], a[rptr]], [lptr, rptr]
            if lptr>=rptr: done = True
            else: swap(a, lptr, rptr)
        swap(a, st, rptr)
        if verbose: print a, piv, [a[lptr], a[rptr]], [lptr, rptr]
        if st<rptr: qs(a, st, rptr-1)
        if rptr<end: qs(a, rptr+1, end)
        
import random
a = [random.randrange(10) for i in range(5)]
#a = [1, 2, 1, 3, 4]
print a
a_check = a[:]

qs(a, 0, len(a)-1)
a_check.sort()

#print a
print a == a_check


    