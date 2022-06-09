#1- Generators - Premissas

x = [1, 2]
print(dir(x))

print("\n")

y = iter(x)
print(dir(y))

print("\n")

for v in x:
    print(v)