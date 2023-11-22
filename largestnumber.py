def largest_num(arr):
    sort_arr = sorted(arr, reverse=True)
    
    largest_number = sort_arr[:2]
    
    return largest_number
    
    
    
my_arr = [10,4,350,23,90]
result = largest_num(my_arr)
print("Largest Number in an array:",result)

