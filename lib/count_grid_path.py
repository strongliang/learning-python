def count_path(x, y):
    if [x, y] == [0, 0]:
        return 1
    else:
        count = 0
        if x>0: count += count_path(x-1, y) 
        if y>0: count += count_path(x, y-1)
        return count
        
        
print count_path(6, 5)