grades = []  # List to store the grades
total_students = 0  # Counter for the total number of students
passed_students = 0  # Counter for the number of students who passed

print("\nEnter student grades.")
print("Type 'done' to stop.")

while True:
    user_input = input("Enter grade: ")

    # Exit condition if the user types 'done'
    if user_input.lower() == 'done':
        print("\n......Computing......")
        break

    # Check if input is a valid digit (grade)
    if user_input.isdigit():
        grade = int(user_input)

        # Validate that the grade is between 40 and 100 (inclusive)
        if 40 <= grade <= 100:
            grades.append(grade)
            total_students += 1

            # Increment the passed_students count if the grade is 50 or above
            if grade >= 50:
                passed_students += 1
        else:
            print("Invalid grade. Grades must be between 40 and 100.")
    else:
        print("Error. Please enter a valid number.")

# Calculate and display the statistics if there are any valid grades
if grades:
    average_grade = sum(grades) / len(grades)
    passing_percentage = (passed_students / total_students) * 100 if total_students > 0 else 0

    print(f"\nGrades entered: {grades}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Number of students who passed: {passed_students}")
    print(f"Passing percentage: {passing_percentage:.2f}%\n")
    
else:
    print("\nNo valid grades were entered.")
