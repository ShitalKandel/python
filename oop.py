import csv
import os

# Main Class
class CSV_Saver:

    #this method takes the data and file name from input 
    # it opens the file in appen mode and writes the data in new line everytime a input is given
    def write_to_csv(self, data, csv_file):
        with open(csv_file, 'a+', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)


    
    #It opens the file to read if, file doesn't exist it creates an empty file with empty rows 
    #it returns a list of rows from csv
    def read_to_csv(self, csv_file):
        rows = []
        # Check if the file exists, and create an empty file if it doesn't
        if not os.path.exists(csv_file):
            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([])  # Write an empty row
        # Read data from the file
        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        return rows



    #it first reads the file and deletes it by rows wherars, indices are given to delete corresponding files
    #if a valid index is provided it deletes that rows of data
    def delete_row_from_csv(self, csv_file):
        if os.path.exists(csv_file):
            data = self.read_to_csv(csv_file)
            

            #if file exist it list out the data inside the file
            if len(data) > 0:
                print("Existing data with index:")
                for i, row in enumerate(data[1:], 1):
                    print(f"{i}. {row}")
                index = int(input("Enter the index of the data to delete: "))
                

                #if the input index matches the list of data(identify by indcies) inside the file
                #it pops the rows
                if 1 <= index <= len(data) - 1:
                    data.pop(index -0)
                    with open(csv_file, 'w', newline='') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerows(data)
                    print(f"Row at index {index} deleted.")
                else:
                    print(f"Invalid index. No data found at index {index}.")
            else:
                print(f"CSV file {csv_file} is empty. Cannot delete.")
        else:
            print(f"File {csv_file} not found.")



        # if len(data) > 0:
        #     print("Existing data with index:")
        #     for i, row in enumerate(data[1:],1):
        #         print(f"{i}. {row}")
        #     index = int(input("Enter the index of the data to update: ")) 
        #     self.update_to_csv(self.csv_file, index, updated_data[0:])



    #it updates a specific row , and reads the existing data and replace the row of csv_file
    #with new data
    def update_to_csv(self, csv_file, index, updated_data):
        data = self.read_to_csv(csv_file)
        if len(data) > index:
            data[index] = updated_data
            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
        else:
            print(f"Invalid index. No data found at index {index}.")




    #if the file doesn't exist it creates a new file
    @staticmethod
    def create_csv_file(csv_file, header):
        if not os.path.exists(csv_file):
            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(header)



# Child Class
class CSV_Operation(CSV_Saver):

    
    
    #constructor that initializes an instance with a csv_file and header.
    #It also initializes an operation_log list to keep track of CSV operations.
    def __init__(self, csv_file, header):
        super().__init__()
        self.csv_file = csv_file
        self.header = header
        self.operation_log = []  # To keep a record of CSV operations



    #This method creates a new CSV file, logging the operation in the operation_log list.
    def create_csv_file(self):
        data = f"Create CSV File: {self.csv_file}"
        self.operation_log.append(data)
        super().create_csv_file(self.csv_file, self.header)



    #This method updates a specific row in the CSV file. It prints the existing data with 
    # indices, prompts the user to choose an index to update. If a valid index is provided, 
    # it updates the corresponding row and logs the operation.
    def update_csv_file(self, updated_data):

        # operation = f"Update CSV File: {self.csv_file}"
        # self.operation_log.append(operation)

        data = self.read_to_csv(self.csv_file)
        if len(data) > 0:
            print("Existing data with index:")
            for i, row in enumerate(data[1:],1):
                print(f"{i}. {row}")
            index = int(input("Enter the index of the data to update: ")) 
            self.update_to_csv(self.csv_file, index, updated_data[0:])
        else:
            print(f"CSV file {self.csv_file} is empty. Cannot update.")


    #deletes the specific row of the data
    def delete_csv_file(self):
        operation = f"Delete CSV File: {self.csv_file}"
        self.operation_log.append(operation)
        self.delete_row_from_csv(self.csv_file)


    #This method returns the operation_log list, which keeps track of the operations performed on the CSV file.
    def get_operation_log(self):
        return self.operation_log

# Get user input for file name
file_name = input("Enter file name (without extension .csv): ") + ".csv"

# Define the header
header = ["Name", "Age", "City"]

# Check if the file already exists
if os.path.exists(file_name):
    print("File exists. Do you want to fill data, update, or delete? (fill/update/delete):")
    action = input().lower()

    if action == 'fill':
        print("Enter data for each column:")
        data = [input(f"{column}: ") for column in header]
        csv_obj = CSV_Operation(file_name, header)
        csv_obj.create_csv_file()
        csv_obj.write_to_csv(data, file_name)

    elif action == 'update':
        csv_obj = CSV_Operation(file_name, header)
        updated_data = [input(f"{column}: ") for column in header]
        csv_obj.update_csv_file(updated_data)

    elif action == 'delete':
        csv_obj = CSV_Operation(file_name, header)
        csv_obj.delete_csv_file()

    else:
        print("Invalid action. Please choose fill, update, or delete.")
else:
    print("Your new file name:", file_name)
    csv_obj = CSV_Operation(file_name, header)
    csv_obj.create_csv_file()

    data = [input(f"{column}: ") for column in header]
    csv_obj.write_to_csv(data, file_name)

# Print the operation log
print("Operation Log:")
print(csv_obj.get_operation_log())
