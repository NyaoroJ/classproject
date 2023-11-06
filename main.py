# Sample student data dictionary (student ID as the key and the corresponding year as the value)
student_data = {
    "2023XYZ1234": "3rd year",
    "2022ABC5678": "2nd year",
    "2021DEF9012": "1st year",
}
def verify_student_id_and_year():
    student_id = input("Enter your student ID: ")

    if student_id in student_data:
        year = student_data[student_id]
        print(f"Student ID {student_id} is in the {year}.")
        marks = int(input("Enter your marks: "))

        # Your grading logic here (e.g., pass/fail based on marks)
        if marks >= 50:
            print("You have passed the exam.")
        else:
            print("You have failed the exam.")
    else:
        print("Invalid student ID. Please check and try again.")


# Example usage:
verify_student_id_and_year()
