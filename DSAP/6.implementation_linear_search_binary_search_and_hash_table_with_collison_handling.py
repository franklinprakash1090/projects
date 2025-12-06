# Linear Search Implementation
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Return the index of the element
    return -1  # Element not found


# Binary Search Implementation
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  # Return the index of the element
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found


# Hash Table with Collision Handling (Chaining)
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create empty chains

    def hash_function(self, key):
        return key % self.size  # Simple hash function

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)  # Insert at the end of the chain

    def search(self, key):
        index = self.hash_function(key)
        for element in self.table[index]:
            if element == key:
                return index, self.table[index].index(key)  # Found at the chain
        return -1  # Element not found


# Driver Code

# Linear Search
arr = [10, 20, 30, 40, 50, 60]
key = 30
print(f"Linear Search Result: Index {linear_search(arr, key)}")

# Binary Search (Array must be sorted)
arr = [10, 20, 30, 40, 50, 60]
key = 30
print(f"Binary Search Result: Index {binary_search(arr, key)}")

# Hash Table
hash_table = HashTable(10)
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)
hash_table.insert(45)

key = 25
print(f"Hash Table Search Result: Found at Index {hash_table.search(key)}")
