def decorator_function(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper
@decorator_function
def message():
    print("hello python")
message() 