#1- kwargs - unpacking

def main(name, last_name, age):
    print(f"Full name: {name} {last_name}")
    print(f"Age: {age}")

data = {
    "name": "Joao",
    "last_name": "Filho",
    "age": 30
}

main(**data)