#1- context manager - ex2 (gerenciamento de recurso)

files = []
for x in range(100000):
    with open("arquivo.txt") as file:
        files.append(file)