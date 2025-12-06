# Bubble Sort in Python


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, array is already sorted
        if not swapped:
            break


# Driver Code
data = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", data)

bubble_sort(data)
print("Sorted Array:", data)
