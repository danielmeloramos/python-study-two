#1- Decorators - Premissas
# funcoes podem ser passadas como parametro de outras funcoes
def function_call(func):
    number_to_add = 5
    return func(number_to_add)

print(function_call(lambda x: x + 1))