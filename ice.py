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
        '1': 60,
        '2': 40,
        '3': 50
    }
def add_flavors():
    
    user_input = int(input("Select an ice cream flavor (1-5): "))
    if user_input not in flavors_prices:
        print("Invalid input")
        return flavors_prices.get(6,0)
    else:
        print("Valid Flavor Price")
    selected_flavor = flavors_prices.get(user_input, 0)
    return selected_flavor

def add_toppings():
    
    choosen_toppings = []
    total_toppings_price = 0
    while True:
        user_input = input("Select additional topping from 1-3, type 'done' when finish): ")
        if user_input.lower() == 'done':
                break
        elif user_input in toppings_prices:
            print("Valid Toppings Price")
            # total_toppings_price += toppings_prices.get(int(user_input), 0)
            total_toppings_price += toppings_prices[user_input]
            choosen_toppings.append(user_input)#total_toppings_price
        else:
            print("Invalid input for toppings")
    return total_toppings_price , choosen_toppings

def calculate_total(selected_flavor, choosen_toppings):
    # ice_cream_price = selected_flavor
    # toppings_price = sum(choosen_toppings)
    # total_price = ice_cream_price + toppings_price
    return selected_flavor + choosen_toppings 

def print_bill(selected_flavor, choosen_toppings, total_price):
    print("----- Bill -----\n")
    print(f"Selected Ice Cream: Rs.{selected_flavor:.2f}")
    print("Selected Toppings:")
    # for tooping in choosen_toppings:
        # print(f"{toppings_prices}")
    print(f"Total Price: Rs.{total_price:.2f}")

#add date time
    with open("ice_cream_bill.txt", "a") as file:
        file.write(f"Selected Ice Cream: Rs.{selected_flavor:.2f}\n")
        file.write("Selected Toppings:\n")
        for topping in choosen_toppings:
            file.write(f"{toppings_prices}")
        
        file.write(f"Total Price: Rs.{total_price:.2f}\n\n")

def get_fun():
    flavor = int(input("Selected flavor : "))
    while flavor not in flavors_prices:
        flavor = int(input("Please re-order the flavor : "))
    return flavors_prices.get(flavor)
        
        
             
def main():
    display_menu()
    flavor_price = get_fun()
    print(flavor_price)
    extra_topping()
    total_toppings_price,choosen_toppings = add_toppings()  
    print(total_toppings_price)#change choosen toopings into total_toopings_price
    total_price = calculate_total(flavor_price, total_toppings_price)  
    print(total_price)
    print_bill(flavor_price, choosen_toppings, total_price)
    
    


main()