

def partition(numbers):
    left = []
    pivot = numbers[0]
    right = []

    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers

    left, pivot, right = partition(numbers)

    sorted_array = quicksort(left) + [pivot] + quicksort(right)
    print(sorted_array)
    return sorted_array


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))
