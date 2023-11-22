def selection_sort(arr, size):
    
    for s in range(size):
        min_index = s
        
        for i in range(s+1, size):
            if arr[i] < arr[min_index]:
                min_index = i
                
        arr[s], arr[min_index] = arr[min_index], arr[s]
        
# Example usage
arr_list = [3,8,1,4,6]
size = len(arr_list)
selection_sort(arr_list, size)

print("Seleection Sort Example")
print(arr_list)
        