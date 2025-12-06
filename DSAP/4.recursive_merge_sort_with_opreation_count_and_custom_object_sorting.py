# Global operation counter
operation_count = 0


# Merge function with operation count
def merge(left, right):
    global operation_count
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        operation_count += 1  # Counting comparison

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Recursive Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Custom Object Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name}-{self.marks}"


# Custom merge function for student objects
def merge_custom(left, right):
    global operation_count
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        operation_count += 1

        if left[i].marks <= right[j].marks:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Recursive merge sort for students
def merge_sort_custom(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_custom(arr[:mid])
    right = merge_sort_custom(arr[mid:])
    return merge_custom(left, right)


# Main program

# Sorting integers
data = [38, 27, 43, 3, 9, 82, 10]
operation_count = 0
sorted_data = merge_sort(data)

print("Sorted Integers:", sorted_data)
print("Total Operations for Integers:", operation_count)

# Sorting custom objects
students = [
    Student("Arun", 88),
    Student("Bala", 75),
    Student("Chitra", 92),
    Student("Divya", 85),
]

operation_count = 0
sorted_students = merge_sort_custom(students)
print("Sorted Students by Marks:", sorted_students)
print("Total Operations for Students:", operation_count)
