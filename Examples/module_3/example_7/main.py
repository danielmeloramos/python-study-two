#1- Decorators 

def uppercase_decorator(function):
    def wrapper():
        result = function()
        make_uppercase = result.upper()
        return make_uppercase
    
    return wrapper

def say_hello():
    return "hello there"

decorate = uppercase_decorator(say_hello)
print(decorate())