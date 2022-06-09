from functools import reduce

def main():
    numbers = [2, 3, 4, 5, 6, 7]
    total_value = reduce(lambda x, y: x + y, numbers)
    print(total_value)

if __name__ == "__main__":
    main()
