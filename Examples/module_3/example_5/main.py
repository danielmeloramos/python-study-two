#1- Decorators - Premissas
# funcoes podem retornar outras funcoes
def hello_function(name):
    def say_hi():
        return f"Hi, {name}!"

    return say_hi

hello = hello_function("Jonh")
print(hello())