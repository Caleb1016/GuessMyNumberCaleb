# Program Name: GuessAreaRectangleYourName

def main():
    print("Welcome to the Guess Area of Rectangle Game!")

    # Ask the user for the length of the rectangle
    length = float(input("Enter the length of the rectangle: "))

    # Ask the user for the width of the rectangle
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the correct area of the rectangle
    correct_area = length * width

    # Ask the user to guess the area
    guessed_area = float(input("Guess the area of the rectangle: "))

    # Check if the guessed area is correct
    if guessed_area == correct_area:
        print("Congratulations! You guessed the area correctly.")
    else:
        print(f"Sorry, that's incorrect. The correct area is {correct_area}.")

# Run the program
if __name__ == "__main__":
    main()