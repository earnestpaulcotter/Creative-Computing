def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the function and get the result
    result = check_even_odd(num)
    
    # Print the message returned by the function
    print(result)

# Run the program
if __name__ == "__main__":
    main()