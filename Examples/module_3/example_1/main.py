#1- context manager

files = []
for x in range(100000):
    files.append(open('requirements.txt', 'r'))