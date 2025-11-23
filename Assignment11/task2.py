from collections import deque

class Queue:
    """
    A simple implementation of a Queue data structure using collections.deque.
    It follows the First-In, First-Out (FIFO) principle.
    """

    def __init__(self):
        """Initializes an empty queue."""
        self._items = deque()

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self._items

    def enqueue(self, item):
        """
        Adds an item to the back (end) of the queue.
        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        Returns:
            The item at the front of the queue.
        Raises:
            IndexError: If dequeue is called on an empty queue.
        """
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def size(self):
        """
        Returns the number of items in the queue.
        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.
        Returns:
            The item at the front of the queue.
        """
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._items[0]

# --- Example Usage ---
if __name__ == "__main__":
    q = Queue()
    print("Is queue empty?", q.is_empty())
    q.enqueue("first")
    q.enqueue("second")
    q.enqueue("third")
    print("Queue size:", q.size())
    print("Front item (peek):", q.peek())
    print("Dequeued item:", q.dequeue())
    print("Front item after dequeue:", q.peek())
    print("Is queue empty?", q.is_empty())
