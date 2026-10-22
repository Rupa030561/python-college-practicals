# Practical 4: Character Classification

DIGIT_NAMES = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR",
    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")

elif ch.isalpha():
    print("It is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")
    elif ch.islower():
        print("It is a lowercase letter.")

elif ch in "0123456789":
    print("It is a numeric digit.")
    print("Digit in words:", DIGIT_NAMES[int(ch)])

elif ch.isspace():
    print("It is a whitespace character.")

else:
    print("It is a special character.")