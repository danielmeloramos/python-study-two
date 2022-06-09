def main():
    numbers = [2, 3, 4, 5, 6, 7]
    pair_numbers = filter(lambda x: x % 2 == 0, numbers)
    print(list(pair_numbers))

if __name__ == "__main__":
    main()