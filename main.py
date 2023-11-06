# Sample student fee status data (student IDs as keys and fee status as values)
fee_status_data = {
    "2023XYZ1234": "Cleared",
    "2022ABC5678": "Cleared",
    "2021DEF9012": "Not Cleared",
}


def verify_fee_status():
    student_id = input("Enter your student ID: ")

    # Check if the input ID is in the fee_status_data dictionary
    if student_id in fee_status_data:
        fee_status = fee_status_data[student_id]
        if fee_status == "Cleared":
            print(f"Student ID {student_id} has cleared the fee.")
        else:
            print(f"Student ID {student_id} has not cleared the fee.")
    else:
        print("Invalid student ID. Please check and try again.")

verify_fee_status()
