#1- Exercicio Generator

def get_impar(values):
    for i in values:
        if i % 2:
            yield i

for x in get_impar(range(200)):
    print(x)