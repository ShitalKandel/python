import datetime


#creating a class ice-cream
class IceCream:

    #we create a method initializer 
    def __init__(self):

        #making a dictonary for ice_-cream and toppings
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

    #This method displays the menu of ice_cream in a readable format
    def display_menu(self, menu):
       
        print(f"\nMenu for {menu}:")

        '''it iterates over the len of menu which contains items  and prices ,
        as indexing starts from 0 it adds +1 so it could start to count from 1 and len of menu'''
        for i in range(1, len(menu) + 1):

            '''here we used list to convert menu(dict) into list(tuple), here i starts from one
            and we want to show numbering starting from 1 not zero, so when we choose 1 it fetches
            the value at index 0'''
            item, price = list(menu.items())[i - 1]
            print(f"{i}. {item} ------ Rs.{price}")
            #it returns menu of ice-cream and toppings with prices


    #this method is responsilbe for taking order/input from customer
    #it takes a parameter menu which iterates the list of ice-cream
    def get_user_input(self, prompt,menu):

        #we use while loop so user can give infinite input until it is true
        while True:

            #this block is used to try any block of code within it so if any error occurs 
            #it will pass the error to it's correspondance
            try:
                user_input = int(input(prompt))

               #we have if statement where it checks if the input is in list of menu, else it gives 
               # invalid input message
                if 1 <= user_input <= len(menu):
                    return user_input
                else:
                    print("Invalid input. Please enter a valid option.")

            #it raised an error if the input from user cannot be converted or isn't an integer
            except ValueError:
                print("Invalid input. Please enter a number.")
                


    '''this method calls display_menu methods as dict where name of ice-cream will be the key and 
    it's correspondance prices'''
    def get_flavor_price(self):
        self.display_menu(self.flavor_prices)

        #this block handles the user input from get_user_input and self.falvor_prices to validate 
        #the input if it is in dict flavor_prices
        user_input = self.get_user_input("Select an ice-cream flavor from the menu: ", self.flavor_prices)

        #this block of code turns the selected input into list and indexes it into list
        selected_flavor = list(self.flavor_prices.keys())[user_input - 1]

        #it returns the price of selected input 
        return self.flavor_prices[selected_flavor]



    '''this method uses self to call the display_menu method with prices of toppings'''
    def extra_topping(self):
        self.display_menu(self.topping_prices)

        #a list is created where it stores toppings from the user input
        chosen_toppings = []

        #here it will continious run until it is closed by the input 0
        while True:
            print("Enter input from 1 to 3 to choose toppings, or 0 to finish:")
            user_input = input()
            if user_input == '0':
                break


            '''here user gives input for toopings which is split 
            the code then uses valid_topping_number to filtering the input keeping only the
            number that matches the dict of toppings_prices'''
            topping_numbers = [int(num) for num in user_input.split(',') if num.isdigit()]
            valid_topping_numbers = [num for num in topping_numbers if 1 <= num <= 3]
            

            #if input doesn't matches the dict it will provides error message
            if not valid_topping_numbers:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue


            #if more than one toopings are selected using the list it get's stored in chosen_toppings 
            chosen_toppings.extend([list(self.topping_prices.keys())[num - 1]
        for num in valid_topping_numbers])


        #total price of toopings are added from the chosen_toppings list
        total_toppings_price = sum(self.topping_prices[topping] for topping in chosen_toppings)

        #it returns the prices of toppings and key of the toppings_price from dict
        # and from the list of chosen_toppings
        return total_toppings_price, chosen_toppings
    
    
    '''this method uses self to call the display_menu method with prices of ice-cream flavor
     and total price of choosen toppings of sizes'''
    def calculate_total_price(self, flavor_price, total_toppings_price):

        #it returns the sum of flavor_price and toppings price
        return flavor_price + total_toppings_price
    

    #it takes 3 parameters which are calculated on other instances of class
    def print_bill(self, flavor_price, chosen_toppings, total_price):


        #printing out all the information about the bill
        print("\nYour Bill:")

        #it returns the flavor prices from the user_input
        print(f"Flavor Price: Rs.{flavor_price}")
        print("Chosen Toppings:")

        #for loop iterates over each element in chosen_toppings
        for topping in chosen_toppings:
            print(f"- {topping}")

        #it prints the total toppings price by subtracting total price with flavor price
        print(f"Total Toppings Price: Rs.{total_price - flavor_price}")

        #it prints total price including flavors of ice-cream and toppings
        print(f"Total Price: Rs.{total_price}")

#
def main():
    
    #an instance of IceCream class is create
    ice_cream_shop = IceCream()

    '''It calls the IceCream class and it's result is stored in
    flavor_price , this method allows user to choose flavor from input and returns
    it's corresponding prices'''
    flavor_price = ice_cream_shop.get_flavor_price()


    '''This method asks user to enter their desired toppings and then checks if they exist or not'''
    total_toppings_price, chosen_toppings = ice_cream_shop.extra_topping()

    '''calculate total price is called from class IceCream which likely passes and returns 
    flavor price and total toppings price'''
    total_price = ice_cream_shop.calculate_total_price(flavor_price, total_toppings_price)


    #print bill method of IceCream is called displaying the bill based on the flavor price,
    #chosen toppings and total price
    ice_cream_shop.print_bill(flavor_price, chosen_toppings, total_price)

    #it gives exact time when order for ice-cream flavor and toppings is given
    time = datetime.datetime.now()
    print(f"\nOrder placed on {time}")


if __name__ == "__main__":
    main()
