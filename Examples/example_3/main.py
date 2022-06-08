#Tratando e repassando excecoes
class InvalidPersonName(Exception):
    pass

class InvalidPersonAge(Exception):
    pass

class Person():
    def __init__(self, name, age):
        if len(name) < 2:
            raise InvalidPersonName()
        if age < 0 or age > 150:
            raise InvalidPersonAge()

        self.name = name
        self.age = age

try:
    name = input("Digite o nome: ")
    age = int(input("Entre com sua idade: "))
    person = Person(name, age)
except InvalidPersonName:
    print("Nome é inválido")
except InvalidPersonAge:
    print("Idade é inválida")
except ValueError:
    print("Nome ou Idade é inválida.")
else:
    print("Pessoa Criada!")
