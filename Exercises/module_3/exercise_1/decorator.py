from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        time_one = time()
        result = func(*args, **kwargs)
        time_two = time()
        print(f'Function {func.__name__!r} executed in {(time_two-time_one):.4f}s')
        return result
    return wrap_func

@timer_func
def loop():
    for n in range(0, 10000000):
        pass

@timer_func
def loop_while():
    count = 0
    while count < 10000000:
        count += 1

if __name__ == "__main__":
    loop()
    loop_while()
