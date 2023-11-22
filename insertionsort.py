def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        
        a = arr[i]
        j = i -1
        while j >=0 and a < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
            
            arr[j + 1]= a
        return arr
            
arr = [7,4,5,2,1]
insertion_sort(arr)

print("Insertion Sorting Example")
sorted_arr = insertion_sort(arr)
print(sorted_arr)

