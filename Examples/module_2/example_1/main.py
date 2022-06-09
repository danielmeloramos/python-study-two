#1- args

def average(*args):
    return sum(args) / len(args)

print(average(2, 2, 2))
# Saída: 2.0

print(average(5, 10))
# Saída: 7.5