#1- Decorators - Premissas
# Funcoes dentro de funcoes
def plus_one(number):
    def add_one(num):
        return num + 1

    result = add_one(number)
    return result

print(plus_one(4))