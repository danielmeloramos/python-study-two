#1- Sem List Comprehensions - Exempplo Numeros impares

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new = [num for num in numbers if num % 2 != 0]
print(new)