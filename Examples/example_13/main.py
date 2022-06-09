#1- Filters

#Sem filter
number_list = range(-5, 5)
less_than_zero = []
for x in number_list:
    if x < 0:
        less_than_zero.append(x)
print(less_than_zero)
