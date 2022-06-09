#1- Reduce

#Com reduce
from functools import reduce

my_list = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, my_list)
print(product)