class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node is initially 1


class AVLTree:
    def __init__(self):
        self.root = None

    # Utility function to get the height of the tree
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Utility function to get the balance factor of a node
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right Rotation (RR)
    def right_rotate(self, z):
        y = z.left
        T2 = y.right

        # Perform rotation
        y.right = z
        z.left = T2

        # Update heights
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    # Left Rotation (LL)
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    # Insert a node
    def insert(self, node, key):
        # 1. Perform the normal BST insertion
        if node is None:
            return Node(key)

        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Update the height of the ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 3. Get the balance factor of this ancestor node
        balance = self.balance_factor(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case (LL Rotation)
        if balance > 1 and key < node.left.value:
            return self.right_rotate(node)

        # Right Right Case (RR Rotation)
        if balance < -1 and key > node.right.value:
            return self.left_rotate(node)

        # Left Right Case (LR Rotation)
        if balance > 1 and key > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case (RL Rotation)
        if balance < -1 and key < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the (unchanged) node pointer
        return node

    # Wrapper for insert function
    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # In-order Traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Public method to display the in-order traversal
    def display_inorder(self):
        self.inorder(self.root)
        print()


# Driver Code
avl_tree = AVLTree()

# Insert elements into the AVL Tree
avl_tree.insert_key(30)
avl_tree.insert_key(20)
avl_tree.insert_key(10)  # Will trigger right rotation (LL)
avl_tree.insert_key(25)
avl_tree.insert_key(40)
avl_tree.insert_key(50)
avl_tree.insert_key(60)  # Will trigger left rotation (RR)

# Display tree elements in In-order traversal
print("In-order Traversal of AVL Tree:")
avl_tree.display_inorder()
