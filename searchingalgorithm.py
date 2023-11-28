def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


my_list = [1, 3, 5, 7, 9]
target_value = 5

result = linear_search(my_list, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}.')
else:
    print(f'Target {target_value} not found in the list.')





