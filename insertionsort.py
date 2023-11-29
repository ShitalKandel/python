def insertion_sort(arr):
    

    #this line starts a loop to iterate 
    #over the list of array
    for i in range(1, len(arr)):


     #we create a new variable that stores a sorted array   
        a = arr[i]

        # we use this condition as preceding element in an array(after i)
        j = i -1

        #we create a while loop which measures if a number is greater or equal to the preceding one
        
        while j >=0 and a < arr[j]:

            #thid block of code will change the position of arr[j] to the right
            arr[j+1] = arr[j]
            j = j - 1
            
            arr[j + 1]= a
        return arr
            
arr = [7,4,5,2,1]
insertion_sort(arr)

print("Insertion Sorting Example")
sorted_arr = insertion_sort(arr)
print(sorted_arr)

