def quicksort(arr):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr) // 2]
    left = [x for x in arr if x > op]
    middle = [x for x in arr if x == op]
    right = [x for x in arr if x < op]
    return quicksort(left) + middle + quicksort(right)

numbers = [3, 6, 8, 7, 1, 2, 1]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
