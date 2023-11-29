# import random

# num = int(input("Enter randon number:"))


# random_num = random.randint(5000,num)
        
        
# print ("Random Number is :",random_num)

#sorting algorithm


'''First we make a list of numbers of 20 between 5000-100000, we use random built-in module 
of python to generate random numbers in a traditional way'''


#we created a list to store sorted array
sorted_list = [ ]

#we built a function to short the number in list
def bubble_sort():

    n = len(unsorted)

    #Loop is used to iterate over the unsorted list
    for i in range(len(unsorted)):

        for j in range (0, n-i-1):

            #if num in left first index is greater than the second then swap 
            if unsorted[j] > unsorted[j+1]:
            
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]

    #it returns unsorted list of numbers       
    return unsorted


#we create another function to iterate over the sorted list to give index of targeted num
def target_index(target):
            
    #if targeted num in sorted list  it will provide the position of the targeted num
    #else it will give the postion of nearest num
    if target in sorted_list:
        print("Index of target:", sorted_list.index(target))

    else:
        near_num = min(sorted_list,key=lambda x :abs(x-target))
        print("Nearest Number:",near_num)

    #it returns the position of targeted num or nearest num to the targeted num




#we have another function which searched the targeted num(which we  name as choice)
 

#Searching Algorithm
def binary_Search():
    low = 0
    high = len(sorted_list)

    while low <= high:
        mid = (low+high)//2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    return -1

      

unsorted = [89085,81435,37530,53356,50000,19560,31955,78025,50000,24735,
            46450,46130,48800,51600,25400,35230,49971,1155,80000,60000]
print("Unsorted list are:",unsorted)

target = 49970


#it calls the bubble sort function
sorted_list = bubble_sort()
print("Sorted List are:",sorted_list)

choice = 49972



#Using Binary Searching 
index = binary_Search()


#we use if statement to return the index of choice num else it returns the nearest num
if index != -1:
    print("Binary Search: Index of target:", index)
else:
    print("Binary Search: Target not found")


#num in choice are passed to target index(function) to check if it matches the condition
target_index(choice)




