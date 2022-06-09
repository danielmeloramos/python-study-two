#1- args & kwargs

def foo(*args, **kwargs):
    for arg in args:
        print(f"arg: {arg}")
    for key, value in kwargs.items() : 
        print(f"key: {key}, value: {value}")

foo(1, 2, 3, name="Daniel")