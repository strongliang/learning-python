def foo():
    def bar():
        return "hello world"
    return bar
    
    
print foo()()
