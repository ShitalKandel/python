# Get the file name from user input
file_name = input("Enter the file name: ") + ".csv"
pass
print("this is your file name:",file_name)
# Open the file in write mode ('w')
with open(file_name, 'w') as file:
    # Get data from user input
    data = input("Enter data to be stored in the file: ")

    # Write the data to the file
    file.write(data)

print(f"Data has  written as :{data}")
