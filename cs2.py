def is_valid_password(password, difficulty):
    difficulty = difficulty.capitalize()  # Convert the first letter to uppercase
    if difficulty == "Easy":
        if len(password) >= 6:
            return True, "Password meets the requirements."
        else:
            return False, "Password must be at least 6 characters long."
    elif difficulty == "Medium":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) \
                and any(char.isdigit() for char in password):
            return True, "Password meets the requirements."
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                feedback.append("Missing uppercase letter.")
            if not any(char.islower() for char in password):
                feedback.append("Missing lowercase letter.")
            if not any(char.isdigit() for char in password):
                feedback.append("Missing digit.")
            return False, " ".join(feedback)
    elif difficulty == "Hard":
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) \
                and any(char.isdigit() for char in password) \
                and any(not char.isalnum() for char in password):
            return True, "Password meets the requirements."
        else:
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                feedback.append("Missing uppercase letter.")
            if not any(char.islower() for char in password):
                feedback.append("Missing lowercase letter.")
            if not any(char.isdigit() for char in password):
                feedback.append("Missing digit.")
            if not any(not char.isalnum() for char in password):
                feedback.append("Missing special character.")
            return False, " ".join(feedback)
    else:
        return False, "Invalid difficulty level."


def main():
    # Get user input for password and difficulty level
    password = input("Enter your password: ")
    difficulty = input("Choose difficulty level (Easy, Medium, Hard): ")

    # Convert difficulty to lowercase
    difficulty = difficulty.lower()

    # Check if password meets the requirements based on the selected difficulty level
    valid, message = is_valid_password(password, difficulty)
    print(message)


if __name__ == "__main__":
    main()
