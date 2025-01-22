def histogram(numbers):
    for num in numbers:
        print('*' * num)

string_numbers = input()
numbers = list(map(int, string_numbers.split()))
histogram(numbers)
