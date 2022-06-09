#1- Dict Comprehensions

names = ["Carlos", "Daniel", "Pedro"]
names_by_dict = dict([(name, 10) for name in names])
print(names_by_dict)