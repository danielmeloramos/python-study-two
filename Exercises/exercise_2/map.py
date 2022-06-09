def main():
    numbers = [2, 3, 4, 5, 6, 7]
    sum_numbers = map(lambda x: x * 2, numbers)
    print(list(sum_numbers))

if __name__ == "__main__":
    main()