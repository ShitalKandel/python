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

def add_flavors():
    flavors_prices = {
        1: 120,
        2: 150,
        3: 150,
        4: 100,
        5: 120
    }
    user_input = int(input("Select an ice cream flavor (1-5): "))
    if user_input == flavors_prices:
        print("Valid Flavor Price")
    else:
        print("Invalid Flavor Price")
    selected_flavor = flavors_prices.get(user_input, 0)
    return selected_flavor

def add_toppings():
    toppings_prices = {
        1: 60,
        2: 40,
        3: 50
    }
    choosen_toppings = []
    while True:
        extra_topping()
        user_input = input("Select additional topping from 1-3, type 'done' when finish): ")
        if user_input == toppings_prices:
            print("Valid Toppings Price")
        else:
            print("Invalid Toppings Price")
        if user_input.lower() == 'done':
            break
        selected_topping = toppings_prices.get(int(user_input), 0)
        choosen_toppings.append(selected_topping)
    return choosen_toppings

def calculate_total(selected_flavor, choosen_toppings):
    ice_cream_price = selected_flavor
    toppings_price = sum(choosen_toppings)
    total_price = ice_cream_price + toppings_price
    return total_price

def print_bill(selected_flavor, choosen_toppings, total_price):
    print("----- Bill -----\n")
    print(f"Selected Ice Cream: Rs.{selected_flavor:.2f}")
    print("Selected Toppings:")
    for toppings_price in choosen_toppings:
         print(f"  Rs.{topping_price:.2f}")
    print(f"Total Price: Rs.{total_price:.2f}")


    with open("ice_cream_bill.txt", "a") as file:
        file.write(f"Selected Ice Cream: Rs.{selected_flavor:.2f}\n")
        file.write("Selected Toppings:\n")
        for topping_price in choosen_toppings:
            file.write(f"  Rs.{topping_price:.2f}\n")
        file.write(f"Total Price: Rs.{total_price:.2f}\n\n")
        
def main():
    while True:
        
        display_menu()
        selected_flavor = add_flavors()
        choosen_toppings = add_toppings()

        total_price = calculate_total(selected_flavor, choosen_toppings)
        print_bill(selected_flavor, choosen_toppings, total_price)

        repeat = input("Do you want to order again? (yes/no): ")
        if repeat.lower() != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
