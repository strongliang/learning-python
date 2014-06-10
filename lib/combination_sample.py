def combo(elements, length):
    for i in range(len(elements)):
#        print 'i =', i
        if length == 1:
#            print elements[i]
            yield (elements[i],)
#            return elements[i]
        else:
            for next in combo(elements[i+1:len(elements)], length-1):
#                print (elements[i],) + next
#                print '----------'
                yield (elements[i],) + next
#                return [elements[i]] + [next]
    
    
print list(combo([1, 2, 3, 4], 2))

#combo([1, 2, 3, 4], 2)