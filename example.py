# # # Get the file name from user input
# # file_name = input("Enter the file name: ") + ".csv"
# # pass
# # print("this is your file name:",file_name)
# # # Open the file in write mode ('w')
# # with open(file_name, 'w') as file:
# #     # Get data from user input
# #     data = input("Enter data to be stored in the file: ")

# #     # Write the data to the file
# #     file.write(data)

# # print(f"Data has  written as :{data}")

import sys

try:
    f = open('shital.csv.csv')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise