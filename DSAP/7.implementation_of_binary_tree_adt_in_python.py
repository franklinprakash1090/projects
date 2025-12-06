# Binary Tree Node Class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Binary Tree ADT Class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertion method (simple insert)
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Pre-order Traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # In-order Traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Post-order Traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Search for a node in the tree
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # Delete node (helper function for deletion)
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        # Traverse the tree
        if key < node.value:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.value:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            min_node = self._min_value_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Wrapper methods for traversal
    def display_inorder(self):
        self.inorder(self.root)
        print()

    def display_preorder(self):
        self.preorder(self.root)
        print()

    def display_postorder(self):
        self.postorder(self.root)
        print()


# Driver Code
bt = BinaryTree()

# Insert nodes
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)

# Display tree elements in different traversals
print("In-order Traversal: ", end="")
bt.display_inorder()

print("Pre-order Traversal: ", end="")
bt.display_preorder()

print("Post-order Traversal: ", end="")
bt.display_postorder()

# Search for a value
key = 40
found_node = bt.search(key)
print(f"Node with value {key} {'found' if found_node else 'not found'}.")

# Deletion of a node
bt.delete(20)
print("In-order Traversal after deletion of 20: ", end="")
bt.display_inorder()
