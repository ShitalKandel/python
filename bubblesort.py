def bubble_sort(arr):
    n = len(arr)
    
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                return arr

arr = [5,2,9,1,5]
      
bubble_sort(arr)
print(bubble_sort)

print("Bubble Sort Example")
for i in range (len(arr)):
    print("%d" %arr[i])
    



