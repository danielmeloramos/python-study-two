from functools import reduce

def main():
    animals = [
        {"name": "Garfield", "kind": "cat", "age": 2},
        {"name": "Pateta", "kind": "dog", "age": 6},
        {"name": "Mingau", "kind": "cat", "age": 3},
        {"name": "Nemo", "kind": "fish", "age": 1},
        {"name": "Scooby Doo", "kind": "dog", "age": 4},
        {"name": "Mordecai", "kind": "bird", "age": 2},
        {"name": "Pluto", "kind": "dog", "age": 9},
    ]
    animals_dog = filter(lambda x: x["kind"] == "dog", animals)
    animals_dog_age = map(lambda x: x["age"] * 7, animals_dog)
    animals_dog_age_sum = reduce(lambda x, y: x + y, animals_dog_age)
    print(animals_dog_age_sum)
    print(sum(animal["age"] * 7 for animal in animals if animal["kind"] == "dog"))

    #133

if __name__ == "__main__":
    main()
