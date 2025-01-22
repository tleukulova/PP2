def check(num):
    """Check if a number is prime."""
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if check(num)]

numbers_str = input("Enter numbers separated by spaces: ")
#convert string to list
numbers_list = list(map(int, numbers_str.split()))
prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)
