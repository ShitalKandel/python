import csv
import os

# Main Class
class CSV_Saver:
        
    
    def write_to_csv(cls, data, csv_file, header=True):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            
            if header:
                csv_writer.writerow(data[0])
                csv_writer.writerows(data[1:])
            else:
                csv_writer.writerows(data)

    
    def read_to_csv(cls, csv_file):
        rows = []
        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        return rows

    
    def delete_to_csv(cls, csv_file):
        if os.path.exists(csv_file):
            os.remove(csv_file)
            print(f"File {csv_file} deleted.")
        else:
            print(f"File {csv_file} not found.")

    def update_to_csv(cls, csv_file):
        data = cls.read_to_csv(csv_file)
        
        # Check if there is at least one row in the CSV file before updating
        if len(data) > 0:
            data[0][3] = "Updated Data"  
            cls.write_to_csv(data, csv_file)
        else:
            print(f"CSV file {csv_file} is empty. Nothing to update.")

    @staticmethod
    def create_csv_file(csv_file, header):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)


# Child Class
class CSV_Operation(CSV_Saver):
    

    @classmethod
    def __init__(self, data, csv_file, header):
        super().__init__()
        self.csv_file = csv_file
        self.data = data
        self.header = header
        
    
    def write_to_csv(self):
        super().write_to_csv(self.data, self.csv_file)

    def create_csv_file(self):
        super().create_csv_file(self.csv_file, self.header)

    def read_to_csv(self):
        return super().read_to_csv(self.csv_file)

    def delete_to_csv(self):
        super().delete_to_csv(self.csv_file)

    def update_to_csv(self):
        super().update_to_csv(self.csv_file)


data = [
    ["Name", "Age", "City", "Skill"],
    ["John Wick", 25, "Lalitpur", "Actor"],
    ["Roman Range", 30, "Kathmandu", "Fake Wrestler"],
    ["Bob Marley", 22, "Bhaktapur", "Artist"]
]


obj = CSV_Operation().create_csv_file(data,"python.csv", ["Name", "Age", "City", "Skills"])
# obj.create_csv_file("Name", "Age", "City","Skill")
# obj.write_to_csv()
# obj.read_to_csv()
# obj.update_to_csv()
# obj.delete_to_csv()

# obj =CSV_Operation(data, "python.csv", ["Name", "Age", "City", "Skills"])
# obj.write_to_csv()

# CSV_Operation(data, "python.csv", ["Name", "Age", "City", "Skills"]).write_to_csv()

# obj.write_to_csv()

# CSV_Operation.write_to_csv()
# print(CSV_Operation(data, "python.csv", ["Name", "Age", "City", "Skills"]).write_to_csv())

# CSV_Operation.update_to_csv()
# CSV_Operation.delete_to_csv()


