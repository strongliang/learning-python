def round_up(a):
    str_a = str(a+0.5)
    return str_a[:str_a.find('.')]
    
print round_up(27.45)
