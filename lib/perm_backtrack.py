def permute(a, i):
    if i == len(a): print a
    else:
        for j in range(i, len(a)): 
            a[i], a[j] = a[j], a[i]
            permute(a, i+1) 
            a[i], a[j] = a[j], a[i]
            
            
            
permute([1, 2, 3], 0)