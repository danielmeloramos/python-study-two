#1- Generators - 1-Functions/2-Expressions

#1
def gerador():
    for i in range(10):
        yield i * 2

for num in gerador():  
    print(num)

print("\n")

#2
numbers = [1, 2, 3, 4, 5, 6]
lazy_squares = (x * x for x in numbers)
for i in lazy_squares:
    print(i)