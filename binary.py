def binary_search(my_num,target):

    i = 0
    n = len(my_num)

    while i < n:
        m = (i + n)//2

        if my_num[m] == target:
            return my_num[m]
        elif my_num[m] <= target:
            n = m + 1

        else:
            i = m + 1

my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = binary_search(my_num, target)
print(result)  


if result != -1:
    print(f"Target {target} found at index {result} in the sorted list.")
else:
    print(f"Target {target} not found in the sorted list.")
