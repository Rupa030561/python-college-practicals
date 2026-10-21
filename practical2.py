# Practical 2: Prime Numbers


def is_prime(num):
    """Return True if num is a prime number, otherwise False."""
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_integer(prompt):
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


n = get_integer("Enter a number n: ")


# Part A: Check whether n is prime
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")


# Part B: Generate all prime numbers till n
print("\nPrime numbers till", n, "are:")

for num in range(2, n + 1):
    if is_prime(num):
        print(num, end=" ")

print()


# Part C: Generate the first n prime numbers
print("\nFirst", n, "prime numbers are:")

count = 0
num = 2

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1

print()