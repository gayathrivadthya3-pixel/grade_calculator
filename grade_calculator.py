# Function to calculate grade and message
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining! "
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! "
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better! "
    elif 60 <= marks <= 69:
        return "D", "Nice try! Work a little harder! "
    else:
        return "F", "Don't give up! Practice makes perfect! "


# Main program
def main():
    name = input("Enter student name: ")

    # Input validation using while loop
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    grade, message = calculate_grade(marks)

    # Output
    print("\n RESULT FOR", name.upper() + ":")
    print("Marks:", str(marks) + "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run the program
main()