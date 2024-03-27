def adjust_light(level):
    if level == 0:
        print("The light is off (0%).")
        return False  # Indicate to stop the loop
    elif level == 1:
        print("The light is set to Low (25%).")
    elif level == 2:
        print("The light is set to Medium (50%).")
    elif level == 3:
        print("The light is set to High (75%).")
    elif level == 4:
        print("The light is set to Maximum (100%).")
    else:
        print("Invalid input. Please enter a number between 0 and 4.")
    return True  # Continue the loop


def main():
    while True:
        print("Light Dimmer Switch:")
        print("0: Off (0%)")
        print("1: Low (25%)")
        print("2: Medium (50%)")
        print("3: High (75%)")
        print("4: Maximum (100%)")

        choice = input("Enter your choice (0-4): ")

        if choice.isdigit():
            level = int(choice)
            if 0 <= level <= 4:
                if not adjust_light(level):
                    break  # Exit the loop if adjust_light returns False
            else:
                print("Invalid input. Please enter a number between 0 and 4.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
