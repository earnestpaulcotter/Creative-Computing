# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user what to search for
search_name = input("Enter the name to search for: ")

# Search for the name (case-insensitive)
if search_name.capitalize() in names:
    print(f"{search_name} was found in the list!")
else:
    print(f"{search_name} was not found in the list.")