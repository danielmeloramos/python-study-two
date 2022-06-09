#1- Exercicio Generator - Plus (Fibonacci)

def get_fibonacci(count_number):
    num = 0
    num_a = 1
    num_b = 0
    i = 0
    while i < count_number:
        num = num_a + num_b
        num_b = num_a
        num_a = num
        i += 1
        yield num_a

for x in get_fibonacci(20):
    print(x)