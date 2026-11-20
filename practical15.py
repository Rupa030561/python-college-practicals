class InvalidNameError(Exception):
    """Custom exception raised when a name contains digits or special characters."""
    pass


def get_valid_name():
    try:
        name = input("Enter your name: ").strip()

        if not name:
            raise InvalidNameError("Name cannot be empty.")

        # Allow alphabetic characters and spaces (e.g., for first and last name)
        if not all(char.isalpha() or char.isspace() for char in name):
            raise InvalidNameError("Invalid name! Name must not contain digits or special characters.")

        print(f"Valid name entered: {name}")

    except InvalidNameError as e:
        print("Error:", e)


# --- Testing the function ---
get_valid_name()