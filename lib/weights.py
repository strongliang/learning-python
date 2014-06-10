from itertools import *

def isMeasureable(weights, target):
    if target > sum(weights):
        return False
    else:
        combos = []
        for i in range(len(weights)):
            combos += list(combinations(weights, i+1))
        for c in combos:
            if sum(c) == target:
                print c, target
                return True
        res = 0
        for w in weights:
            less_weight = weights[:]
            less_weight.remove(w)
            res += isMeasureable(less_weight, target+w)
            
        return res>0
        
        
print isMeasureable([1, 2, 5, 10, 20, 50, 100], 77)