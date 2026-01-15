#Initalization of inventory and stock
drinks = {
    'drink1': {'item_name': 'Coca Cola', 'item_type': 'Cold Beverage','item_code': 'A1', 'price': 2.50, 'storage': 10},
    'drink2': {'item_name': 'Nescafe Coffee', 'item_type': 'Warm Beverage','item_code': 'A2', 'price': 5.00, 'storage': 10},
    'drink3': {'item_name': 'Lipton Iced Tea', 'item_type': 'Cold Beverage','item_code': 'A3', 'price': 2.50, 'storage': 10},
    'drink4': {'item_name': 'Redbull', 'item_type': 'Cold Beverage','item_code': 'A4', 'price': 10.00, 'storage': 10},
    'drink5': {'item_name': 'Vimto', 'item_type': 'Cold Beverage','item_code': 'B1', 'price': 3.75, 'storage': 10},
    'drink6': {'item_name': 'PRIME', 'item_type': 'Cold Beverage','item_code': 'B2', 'price': 15.50, 'storage': 10},
    'drink7': {'item_name': 'Pocari Sweat', 'item_type': 'Cold Beverage','item_code': 'B3', 'price': 5.00, 'storage': 10},
    'drink8': {'item_name': 'Green Tea', 'item_type': 'Warm Beverage','item_code': 'B4', 'price': 7.50, 'storage': 10},
}
snacks = {
    'snack1': {'item_name': 'Ham Sandwich', 'item_type': 'Heavy Snack','item_code': 'C1', 'price': 7.50, 'storage': 10},
    'snack2': {'item_name': 'Oreo', 'item_type': 'Light Snack','item_code': 'C2', 'price': 3.75, 'storage': 10},
    'snack3': {'item_name': 'Lays Chips', 'item_type': 'Heavy Snack','item_code': 'C3', 'price': 9.50, 'storage': 10},
    'snack4': {'item_name': 'Reeses Nut Bar', 'item_type': 'Light Snack','item_code': 'C4', 'price': 3.75, 'storage': 10},
    'snack5': {'item_name': 'Doritos', 'item_type': 'Heavy Snack','item_code': 'D1', 'price': 8.25, 'storage': 10},
    'snack6': {'item_name': 'KitKat', 'item_type': 'Light Snack','item_code': 'D2', 'price': 2.25, 'storage': 10},
    'snack7': {'item_name': 'Cheetos', 'item_type': 'Heavy Snack','item_code': 'D3', 'price': 9.00, 'storage': 10},
    'snack8': {'item_name': 'OUT OF STOCK', 'item_type': 'N/A','item_code': 'D4', 'price': 0.00, 'storage': 0},
}
#The first two functions are the two dictionaries containing the 'drinks', 'snacks', and store information regarding if an item is hot, cold, light, heavy. The price of each item, it's code, name, and the amount that is left in the storage.

inventory = {'drinks': drinks, 'snacks': snacks}

#The second function is another dictionary called 'inventory'. It's used to consolidate drinks and snacks under respective keys.

#Defs
def display_inventory(): #This def is used to display the inventory.
    print("\nCurrent Inventory:")
    for category, items in inventory.items():
        print(f"\n{category.title()}:")
        for item in items.values():
            print(f" - {item['item_code']} | {item['item_name']} | ${item['price']:.2f} | Stock: {item['storage']}")



def find_product(item_code): #This def is used to validate an user input. In order to vvalidate a users input, it will search for a product based on it's item code. This is case-insensitive.
    for items in inventory.values():
        for item in items.values():
            if item['item_code'].lower() == item_code.lower():
                return item
    return None

def calculate_total(cart): #This def calcualtes the total cost of any and all items that is in the user_cart. It uses sum() to add up the price of each item.
    return sum(item['price'] for item in cart)

def process_payment(total_cost): #This def prompts the user for their payment. Ensures the users input is valid via float.
    while True:
        try:
            payment = float(input(f"\nYour total is ${total_cost:.2f}. Please enter your payment: "))
            if payment >= total_cost:
                return payment - total_cost #If the users payment is sufficient, it will calculate and return change if any
            else:
                print(f"Insufficient funds. You need ${total_cost - payment:.2f} more.") 
        except ValueError:
            print("Invalid input. Please enter a valid amount.") #If the users payment is insufficient, it will notify the user then loop back to the initial prompt

def suggest_item(current_item_type): #This def suggests item based on the item_type of the last item that was placed in the user_cart.
    suggestions = {
        'Cold Beverage': 'Heavy Snack',
        'Warm Beverage': 'Light Snack',
        'Heavy Snack': 'Cold Beverage',
        'Light Snack': 'Warm Beverage'
    } #Uses another dictionary to map item types to suggested types.
    return suggestions.get(current_item_type, None)

def display_filtered_inventory(item_type): #This def only prints items based on their item_type. Filters items that match the item_type and are in stock.
    print(f"\nSuggested items ({item_type.title()}):")
    for category, items in inventory.items():
        for item in items.values():
            if item['item_type'] == item_type and item['storage'] > 0:
                print(f" - {item['item_code']} | {item['item_name']} | ${item['price']:.2f} | Stock: {item['storage']}")

#Main Program
def vending_machine(): 
    while True:
        print("\nHello!! I am a Vending Machine!")
        user_cart = [] #Initalizes user_cart
        suggestion_made = False

        if input("Would you like to see the inventory? (Y/N): ").strip().lower() == 'y':
            display_inventory() #Checks if user input = 'y' and if it's True, it calls the function vending_machine(). 


#Product Selection
        while True:
            item_code = input("\nEnter the item code of the product you want to purchase [or type 'done' to finish]): ").strip()
            if item_code.lower() == 'done':
                break #Prompts the user to either enter an item code to select an item or type 'done' to finish. Calls find_product()
            product = find_product(item_code)

            if product:
                if product['storage'] > 0: #Checks IF the users selected item is in stock via checking if the items storage is above 0.
                    print(f"{product['item_name']} costs ${product['price']:.2f}.")
                    user_cart.append(product)
                    product['storage'] -= 1
                    print(f"{product['item_name']} added to your cart.") #If this inital check is passed, the item is added to user_cart then deducted from the vending machine storage.

                    if not suggestion_made:
                        suggested_type = suggest_item(product['item_type']) #If no suggestions have been made yet, program will call suggest_item() to recommend another catagory, then displays a filtered inventory if the user opts to see suggestions
                        if suggested_type:
                            if input(f"Would you like to see items of type '{suggested_type}'? (Y/N): ").strip().lower() == 'y':
                                display_filtered_inventory(suggested_type)
                        suggestion_made = True
                else:
                    print(f"Sorry, {product['item_name']} is out of stock.") #If the product is out of stock.
            else:
                print("Invalid item code. Please try again.") #If user input is invalid.

#Checkout process
        if user_cart:   #if the user_cart is not empty the program displays all items in the cart.
            print("\nYour cart:")
            for item in user_cart:
                print(f" - {item['item_name']} | ${item['price']:.2f}")
            total_cost = calculate_total(user_cart) #calls calculate_total() to calcualte total cost
            change = process_payment(total_cost) #handles payment.

            print("\nTransaction successful!") #If the transaction is successful, user is notified
            if change > 0:
                print(f"Your change is: ${change:.2f}") #if there is change it will display user change.
            print("Thank you for your purchase!")
        else:
            print("Your cart is empty.") #If cart is empty, the user is notified

#Loop Control
        if input("\nWould you like to make another purchase? (Y/N): ").strip().lower() != 'y': #Prompt if user would like to make another purchase
            print("Thank you for using my services!! Till next time!")
            break #If the user declines program ends with a goodbye message.


if __name__ == "__main__":
    vending_machine()
    
#Calls the vending_machine() def to start the program

#lines 83-135 is the main vending machine code. It's comprised of all the prompts unlike the others