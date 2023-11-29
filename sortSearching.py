# import random

# num = int(input("Enter randon number:"))


# random_num = random.randint(5000,num)
        
        
# print ("Random Number is :",random_num)

#sorting algorithm

sorted_list = [ ]

def bubble_sort():

    n = len(unsorted)
    for i in range(len(unsorted)):
        for j in range (0, n-i-1):

            if unsorted[j] > unsorted[j+1]:
            
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
            
    return unsorted

def target_index(target):
            
    if target in sorted_list:
        print("Index of target:", sorted_list.index(target))

    else:
        near_num = min(sorted_list,key=lambda x :abs(x-target))
        print("Nearest Number:",near_num)
    

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

sorted_list = bubble_sort()
print("Sorted List are:",sorted_list)

choice = 49972




index = binary_Search()

if index != -1:
    print("Binary Search: Index of target:", index)
else:
    print("Binary Search: Target not found")

# Using linear search for target index or nearest number
target_index(choice)




