def fib(a):
    if a==0 or a==1: return a
    prev = 0
    current = 1
    for i in range(1, a):
        current, prev = prev+current, current
    return current
    
print fib(36) == 14930352  
print fib(10)