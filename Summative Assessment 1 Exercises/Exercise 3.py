def get_info():
    # List of keys representing student attributes
    student_keys = ['Name', 'ID Number', 'Age', 'Number', 'Level', 'Course']
    # Dictionary to store student information
    student_dict = {}

    # Loop through each key to collect information
    for key in student_keys:
        if key == 'Age':
            # Input validation for age
            while True:
                value = input(f"Enter {key}: ")
                if value.isdigit(): # Check if the input is numeric
                    student_dict[key] = int(value) # Store age as an integer
                    break
                else:
                    print("Please enter a valid numeric age.") # Error message for invalid input
        else:
            value = input(f"Enter {key}: ") # Collect other information
            student_dict[key] = value # Store the input in the dictionary
    return student_dict # Return the populated dictionary

# Function call to collect student information
Studentinfo = get_info()