#1- Decorators 

def memoize(obj):
    obj._cache = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in obj._cache:
            obj._cache[key] = obj(*args, **kwargs)
        return obj._cache[key]
    
    return memoizer

@memoize
def foo(a, b):
    return a * b

print(foo("ha", 3))

print(foo("ha", 3))