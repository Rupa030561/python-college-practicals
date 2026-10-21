import math

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

a = get_float("Enter the value of a: ")
b = get_float("Enter the value of b: ")
c = get_float("Enter the value of c: ")

if a == 0:
    print("This is not a quadratic equation.")
    if b != 0:
        print("It is linear. Root =", -c / b)
    elif c == 0:
        print("Every x is a solution (0 = 0).")
    else:
        print("No solution.")
else:
    D = b**2 - 4*a*c

    if math.isclose(D, 0, abs_tol=1e-12):
        root = -b / (2*a)
        print("The roots are real and equal.")
        print("Root =", root)

    elif D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print("The roots are real and different.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)

    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*abs(a))
        print("The roots are complex.")
        print("Root 1 =", complex(real_part, imaginary_part))
        print("Root 2 =", complex(real_part, -imaginary_part))