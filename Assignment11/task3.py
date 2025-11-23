class Node:
    """
    A single node in a singly linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        """Initializes a Node with data and a 'next' pointer."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A singly linked list implementation that holds a reference
    to the head node.
    """
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node with the given data at the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the list.
        """
        new_node = Node(data)
        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        # Point the last node to the new node
        last_node.next = new_node

    def display(self):
        """
        Displays the contents of the linked list from head to tail.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements) + " -> None")


# --- Example Usage ---
if __name__ == "__main__":
    llist = SinglyLinkedList()

    print("Inserting 10, 20, 30 at the end:")
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    llist.insert_at_end(30)
    llist.display()

    print("\nInserting 5 at the beginning:")
    llist.insert_at_beginning(5)
    llist.display()

    print("\nInserting 40 at the end:")
    llist.insert_at_end(40)
    llist.display()
