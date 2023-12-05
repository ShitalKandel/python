import csv
import os

# Main Class
class CSV_Saver:
    def write_to_csv(self, data, csv_file, header=True):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            if header:
                csv_writer.writerow(data[0])
                csv_writer.writerows(data[1:])
            else:
                csv_writer.writerows(data)

    def read_to_csv(self, csv_file):
        rows = []
        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        return rows

    def delete_to_csv(self, csv_file):
        if os.path.exists(csv_file):
            os.remove(csv_file)
            print(f"File {csv_file} deleted.")
        else:
            print(f"File {csv_file} not found.")

    def update_to_csv(self, csv_file,index, updated_data):
        data = self.read_to_csv(csv_file)
        if len(data) > index:
            data[index] = updated_data[1]
            self.write_to_csv(data, csv_file,True)
        else:
            print(f"Invalid index. No data found at index {index}.")
           

    @staticmethod
    def create_csv_file(data, csv_file, header):
        with open(csv_file, 'w') as file:
            csv_writer = csv.writer(file)
            if header:
                csv_writer.writerow(data[0])
                csv_writer.writerows(data[1:])
            else:
                csv_writer.writerows(data)
        # CSV_Saver().write_to_csv(data, csv_file, header)


# Child Class
class CSV_Operation(CSV_Saver):
    def __init__(self, csv_file, header):
        super().__init__()
        self.csv_file = csv_file
        self.header = header
        self.operation_log = []  # To keep a record of CSV operations

    def create_csv_file(self, data):
        operation = f"Create CSV File: {self.csv_file}"
        self.operation_log.append(operation)
        self.write_to_csv(data, self.csv_file, self.header)#---

    def update_csv_file(self, updated_data):
        operation = f"Update CSV File: {self.csv_file}"
        self.operation_log.append(operation)
        data = self.read_to_csv(self.csv_file)
        if len(data) > 0:
            print("Existing data with index:")
            for i, row in enumerate(data[1:],1):
                print(f"{i}.{row}")
            index = int(input("Enter the index of the data of update:")) - 1
            self.update_to_csv(self.csv_file, index, updated_data[1])
            # data.append(updated_data[1])
            # self.write_to_csv(data, self.csv_file, self.header)
        else:
            print(f"CSV file {self.csv_file} is empty. Cannot update.")

    def delete_csv_file(self):
        operation = f"Delete CSV File: {self.csv_file}"
        self.operation_log.append(operation)
        super().delete_to_csv(self.csv_file)

    def get_operation_log(self):
        return self.operation_log


# Get user input for file name
file_name = input("Enter file name (without extension .csv): ") + ".csv"
print("This is your file name:",file_name)

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
        csv_obj.create_csv_file([header, data])  # Pass the complete data to update_csv_file

    elif action == 'update':
        csv_obj = CSV_Operation(file_name, header)
        updated_data = [input(f"{column}: ") for column in header]
        csv_obj.update_csv_file([header, updated_data])  # Pass the complete data to update_csv_file

    elif action == 'delete':
        csv_obj = CSV_Operation(file_name, header)
        csv_obj.delete_csv_file()

    else:
        print("Invalid action. Please choose fill, update, or delete.")
else:
    print("File does not exist. Creating a new file...")
    data = [input(f"{column}: ") for column in header]
    csv_obj = CSV_Operation(file_name, header)
    csv_obj.create_csv_file([header, data])

# Print the operation log
print("Operation Log:")
print(csv_obj.get_operation_log())
