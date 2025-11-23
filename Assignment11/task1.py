class Stack:
    """
    A simple implementation of a Stack data structure using a Python list.
    It follows the Last-In, First-Out (LIFO) principle.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self._items

    def push(self, item):
        """
        Adds an item to the top of the stack.
        Args:
            item: The item to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Returns:
            The item at the top of the stack.
        Raises:
            IndexError: If pop is called on an empty stack.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        Returns:
            The item at the top of the stack.
        Raises:
            IndexError: If peek is called on an empty stack.
        """
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def size(self):
        """
        Returns the number of items in the stack.
        Returns:
            int: The number of items in the stack.
        """
        return len(self._items)


# --- Example Usage ---
if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.is_empty())  # Expected: True

    print("\nPushing 1, 2, 'three'")
    s.push(1)
    s.push(2)
    s.push('three')

    print("Is stack empty?", s.is_empty())  # Expected: False
    print("Stack size:", s.size())         # Expected: 3
    print("Top item (peek):", s.peek())    # Expected: 'three'
    print("Popped item:", s.pop())         # Expected: 'three'
    print("Top item after pop:", s.peek()) # Expected: 2
