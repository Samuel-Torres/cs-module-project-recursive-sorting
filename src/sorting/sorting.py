# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    left_index = right_index = 0

    # print('In MERGE =', arrA, '/', arrB)

    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index += 1
            # print('MERGED =', merged_arr)
        else:
            merged_arr.append(arrB[right_index])
            right_index += 1
            # print('MERGED =', merged_arr)
    merged_arr.extend(arrA[left_index:])
    merged_arr.extend(arrB[right_index:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    # endpoint = len(arr) - 1
    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])
    # print('left/right', left, '/', right, 'ARRAY =', arr)

    return merge(left, right)
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
