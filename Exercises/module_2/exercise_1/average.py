from functools import reduce
import json

def calculate_average(*args):
    students_average = []
    for item in args:
        name = item["name"]
        average = round(reduce(lambda x, y: x + y, item["scores"]) / len(item["scores"]))
        student = {"name": name, "average": average}
        students_average.append(student)

    return students_average

try:
    file = open('students.json')  
    data = json.load(file)
    response = calculate_average(*data)
    print(response)
except:
    print("Ocorrer algum erro ao realizar a conversao de media dos alunos")
finally:
    print("Finalinzado a conversao de media dos alunos")