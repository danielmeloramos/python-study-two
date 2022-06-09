#1- args - unpacking

def average(*args):
    return sum(args) / len(args)

values = [3, 4, 4, 6]
print(average(*values))