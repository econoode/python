import functools

def my_decorators(func):
    @functools.wraps(func)
    def function_that_run_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_run_func

@my_decorators
def my_function():
    print("I'm the function")

my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_run_func():
            print("In the decorator!")
            func()
            print("After the decorator!")
        return function_that_run_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

my_function_too()