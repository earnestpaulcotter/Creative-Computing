def days_in_month():    
    # Dictionary mapping month numbers to their respective days
    monthday = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    
    # Attempt to get user input for the month number
    try:
        month = int(input("Input month number (1-12): "))
    except ValueError:
        print("Invalid Input! Please enter a valid number 1-12.")
        return
    
    # Validate the month number
    if month < 1 or month > 12:
        print("Invalid Input! Please enter a valid number 1-12.")
        return
    
    # Handle February's leap year condition
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # Output the number of days for the specified month
        print(f"Month {month} has {monthday[month]} days.")

# Call the function to execute
days_in_month()
