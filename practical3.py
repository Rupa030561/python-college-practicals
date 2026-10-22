# Practical 3: Pyramid and Reverse Pyramid

def print_row(spaces, stars):
    print(" " * spaces + " ".join("*" * stars))

try:
    n = int(input("Enter the number of rows: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        print("\nPyramid:")
        for i in range(1, n + 1):
            print_row(n - i, i)

        print("\nReverse Pyramid:")
        for i in range(n, 0, -1):
            print_row(n - i, i)
except ValueError:
    print("Invalid input. Please enter a whole number.")