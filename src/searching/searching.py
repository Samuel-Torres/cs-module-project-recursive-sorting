# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    middle_index = (start + end) // 2
    val_at_middle = arr[middle_index]
    print('middle index', middle_index)
    print('middle val', val_at_middle)
    print('Target', target)
    print('start', start)
    print('end', end)
    if val_at_middle == target:
        print("Target value found at index:", middle_index)
        return middle_index

    if val_at_middle > target:
        new_end = middle_index - 1
        binary_search(arr, target, start, new_end)
        print('new end adjusted', new_end)
    elif val_at_middle < target:
        new_start = middle_index + 1
        binary_search(arr, target, new_start, end)
        print('new start adjusted', new_start)
    else:
        # print('terminated')
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


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, -8, 0, len(arr1)-1)
