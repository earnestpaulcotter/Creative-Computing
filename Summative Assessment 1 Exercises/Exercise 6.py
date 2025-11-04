cpassword = 300408
attempts = 5

while attempts > 0:
    try: 
        password = int(input("Enter an password: "))
    except ValueError:
         print("Please only input numerical digits. You have remaining!")
         continue
    if password == cpassword:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password! You have {attempts} remaining!")
if attempts == 0:
        print("Too many failed attempts, access DENIED.")