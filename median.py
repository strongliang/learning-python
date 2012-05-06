# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a >= b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median2(a, b, c):
    x = [a, b, c]
    max = biggest(a, b, c)
    total = sum(x)
    for i in range(len(x)):
        if x[i] >= total-max-x[i]:
            return total - x[i]

#def median2(a, b, c):
#    x = [a, b, c]
#    for i in range(len(x)):
#        for j in range(len(x)-i-1):
#            if x[j] is bigger(x[j], x[j+1]):
#                x[j], x[j+1] = x[j+1], x[j]
#    return x[len(x)/2]
           
       
print median2(2, 2, 2)
print median2(3, 3, 5)
print median2(3, 3, 1)
print median2(3, 3, 3)
print median2(3, 1, 2)
print median2(3, 2, 1)
            
    
