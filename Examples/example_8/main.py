#1- Sem List Comprehensions - Exempplo Numeros impares

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new = []
for number in numbers:
    if number % 2 != 0:
        new.append(number)

print(new)