class Node:
    """
    A node in a Binary Search Tree.
    Contains a key and references to left and right children.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """
    A simple Binary Search Tree implementation.
    """
    def __init__(self):
        """Initializes an empty BST with a null root."""
        self.root = None

    def insert(self, key):
        """
        Public method to insert a key into the BST.
        If the tree is empty, the new key becomes the root.
        Otherwise, it calls the private recursive insert method.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """
        Private recursive helper to find the correct position and insert the node.
        It ignores duplicate keys.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def inorder_traversal(self):
        """
        Public method to perform and print an in-order traversal of the tree.
        This will print the keys in sorted order.
        """
        elements = []
        self._inorder_recursive(self.root, elements)
        print("In-order traversal:", " -> ".join(map(str, elements)))

    def _inorder_recursive(self, current_node, elements):
        """
        Private recursive helper for in-order traversal (Left, Root, Right).
        """
        if current_node:
            self._inorder_recursive(current_node.left, elements)
            elements.append(current_node.key)
            self._inorder_recursive(current_node.right, elements)


# --- Example Usage ---
if __name__ == "__main__":
    bst = BST()
    keys_to_insert = [50, 30, 20, 40, 70, 60, 80]
    
    print(f"Inserting keys: {keys_to_insert}")
    for key in keys_to_insert:
        bst.insert(key)

    # In-order traversal of a BST always yields a sorted list
    bst.inorder_traversal()

    print("\nInserting key: 25")
    bst.insert(25)
    bst.inorder_traversal()
