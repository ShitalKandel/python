def display_menu():
    print("Menu for ice-cream")
    print("1. Chocolate ------Rs.120")
    print("2. Strawberry ------Rs.150")
    print("3. Milk Choco ------Rs.150")
    print("4. Caramel ------ Rs.100")
    print("5. Almond ------ Rs.120")

def extra_topping():
    print("\nAdditional Toppings:")
    print("1. Chopped Peanuts ------ Rs.60")
    print("2. Whipped Cream ------ Rs.40")
    print("3. Chocolate Sprinkles ------ Rs.50")
    
    
flavors_prices = {
        1: 120,
        2: 150,
        3: 150,
        4: 100,
        5: 120,
        
}

toppings_prices = {
        1: 60,
        2: 40,
        3: 50
    }
def add_flavors():
    
    user_input = int(input("Select an ice cream flavor (1-5): "))
    if user_input not in flavors_prices:
        print("Invalid input")
        return flavors_prices.get(6,0)
    if user_input in flavors_prices:
        print("Valid Flavor Price")
    else:
        print("Nothing was chosen")
    selected_flavor = flavors_prices.get(user_input, 0)
    return selected_flavor

def add_toppings():
    
    choosen_toppings = []
    total_toppings_price = 0
    while True:
        user_input = input("Select additional topping from 1-3, type 'done' when finish): ")
        if user_input in toppings_prices:
            print("Valid Toppings Price")
    
        else:
            if user_input.lower() == 'done':
                break
        total_toppings_price += toppings_prices.get(int(user_input), 0)
        # choosen_toppings.append(selected_topping)
    return total_toppings_price

def calculate_total(selected_flavor, choosen_toppings):
    # ice_cream_price = selected_flavor
    # toppings_price = sum(choosen_toppings)
    # total_price = ice_cream_price + toppings_price
    return selected_flavor + choosen_toppings

def print_bill(selected_flavor, choosen_toppings, total_price):
    print("----- Bill -----\n")
    print(f"Selected Ice Cream: Rs.{selected_flavor:.2f}")
    print("Selected Toppings:")


    print(f"Total Price: Rs.{total_price:.2f}")


    with open("ice_cream_bill.txt", "a") as file:
        file.write(f"Selected Ice Cream: Rs.{selected_flavor:.2f}\n")
        file.write("Selected Toppings:\n")
        
        file.write(f"Total Price: Rs.{total_price:.2f}\n\n")

def get_fun():
    flavor = int(input("Choosen flavor : "))
    while flavor not in flavors_prices:
        flavor = int(input("Pleased to re-order again : "))
    return flavors_prices.get(flavor)
        
        
             
def main():
    display_menu()
    flavor_price = get_fun()
    print(flavor_price)
    extra_topping()
    choosen_toppings = add_toppings()  
    total_price = calculate_total(flavor_price, choosen_toppings)  
    print(total_price)
    print_bill(flavor_price, choosen_toppings, total_price)
    
    


main()