#1- Exemplo de sorted c/ Lambda
from person import Person

people = [
    Person('Joao', 10),
    Person('Julia', 50),
    Person('Carlos', 25),
    Person('Lucas', 15),
    Person('Mariana', 34)
]

peopleByAge = sorted(people, key=lambda p:p.age)

for person in peopleByAge:
    print(person.name)