#1- context manager - ex3 (gerenciamento de recurso simples)
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename)
        return self.file

    def __exit__(self, *exec):
        self.file.close()

files = []
for x in range(100000):
    with FileManager("arquivo.txt") as file:
        files.append(file)