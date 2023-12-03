import csv
import os
from datetime import datetime

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

    def update_to_csv(self, csv_file):
        data = self.read_to_csv(csv_file)
        if len(data) > 0 and len(data[0])>3 :
            data[0][3] = "Updated Data"
            self.write_to_csv(data, csv_file)
        else:
            print(f"CSV file {csv_file} is empty. Nothing to update.")

    @staticmethod
    def create_csv_file(data, csv_file, header):
        CSV_Saver().write_to_csv(data, csv_file, header)


# Child Class
class CSV_Operation(CSV_Saver):
    def __init__(self, csv_file, header):
        self.csv_file = csv_file
        self.header = header
        self.operation_log = []  # To keep a record of CSV operations with time

    def create_csv_file(self, data):
        # Record the timestamp of the operation
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        operation = f"Create CSV File: {self.csv_file} at {timestamp}"
        self.operation_log.append(operation)

        # Call the method from the parent class to write to the CSV file
        self.write_to_csv(data, self.csv_file, self.header)

    def update_csv_file(self):
        # Record the timestamp of the operation
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        operation = f"Update CSV File: {self.csv_file} at {timestamp}"
        self.operation_log.append(operation)

        # Call the method from the parent class to update the CSV file
        super().update_to_csv(self.csv_file)

    def get_operation_log(self):
        return self.operation_log


# Sample data for testing
data = [
    ["Name", "Age", "City"],
    ["John Wick", 25, "Lalitpur"],
    ["Roman Range", 30, "Kathmandu"],
    ["Bob Marley", 22, "Bhaktapur"]
]

# Create an instance of the CSV_Operation class with CSV file name and header
csv.obj = CSV_Operation("python.csv", ["Name", "Age", "City"])

# Create CSV file and update it
csv.obj.create_csv_file(data)
csv.obj.update_csv_file()

# Print the operation log
print("Operation Log:")
print(csv.obj.get_operation_log())
