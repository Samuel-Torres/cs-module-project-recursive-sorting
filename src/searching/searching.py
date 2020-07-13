# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1

    middle_index = (start + end) // 2
    val_at_middle = arr[middle_index]

    if val_at_middle == target:
        return middle_index
    elif val_at_middle > target:
        new_end = middle_index - 1
        return binary_search(arr, target, start, new_end)
    elif val_at_middle < target:
        new_start = middle_index + 1
        return binary_search(arr, target, new_start, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# print(binary_search(arr1, -8, 0, len(arr1)-1))
