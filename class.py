import datetime

class IceCream:
    def __init__(self):
        self.flavor_prices = {
            "Chocolate": 120,
            "Strawberry": 150,
            "Milk Choco": 150,
            "Caramel": 100,
            "Almond": 120
        }
        self.topping_prices = {
            "Chopped Peanuts": 60,
            "Whipped Cream": 40,
            "Chocolate Sprinkles": 50
        }

    def display_menu(self, menu):
        print(f"\nMenu for {menu}:")
        for i in range(1, len(menu) + 1):
            item, price = list(menu.items())[i - 1]
            print(f"{i}. {item} ------ Rs.{price}")


    def get_user_input(self, prompt, menu):
        while True:
            try:
                user_input = int(input(prompt))
                if 1 <= user_input <= len(menu):
                    return user_input
                else:
                    print("Invalid input. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_flavor_price(self):
        self.display_menu(self.flavor_prices)
        user_input = self.get_user_input("Select an ice-cream flavor from the menu: ", self.flavor_prices)
        selected_flavor = list(self.flavor_prices.keys())[user_input - 1]
        return self.flavor_prices[selected_flavor]

    def extra_topping(self):
        self.display_menu(self.topping_prices)
        chosen_toppings = []
        while True:
            print("Enter input from 1 to 3 to choose toppings, or 0 to finish:")
            user_input = input()
            if user_input == '0':
                break
            topping_numbers = [int(num) for num in user_input.split(',') if num.isdigit()]
            valid_topping_numbers = [num for num in topping_numbers if 1 <= num <= 3]
            
            if not valid_topping_numbers:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue

            chosen_toppings.extend([list(self.topping_prices.keys())[num - 1] for num in valid_topping_numbers])

        total_toppings_price = sum(self.topping_prices[topping] for topping in chosen_toppings)
        return total_toppings_price, chosen_toppings

    def calculate_total_price(self, flavor_price, total_toppings_price):
        return flavor_price + total_toppings_price

    def print_bill(self, flavor_price, chosen_toppings, total_price):
        print("\nYour Bill:")
        print(f"Flavor Price: Rs.{flavor_price}")
        print("Chosen Toppings:")
        for topping in chosen_toppings:
            print(f"- {topping}")
        print(f"Total Toppings Price: Rs.{total_price - flavor_price}")
        print(f"Total Price: Rs.{total_price}")


def main():
    
    ice_cream_shop = IceCream()
    flavor_price = ice_cream_shop.get_flavor_price()
    total_toppings_price, chosen_toppings = ice_cream_shop.extra_topping()
    total_price = ice_cream_shop.calculate_total_price(flavor_price, total_toppings_price)
    ice_cream_shop.print_bill(flavor_price, chosen_toppings, total_price)
    time = datetime.datetime.now()
    print(f"\nOrder placed on {time}")


if __name__ == "__main__":
    main()
