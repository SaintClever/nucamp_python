class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    # Your Challenge:
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)

        # If self object already has a head
        elif self.head is not None:
            self.next = new_node
            print("Prepended new Head Node with value:", self.next.value)
            print("Node following Head is:", self.head.value)


# Testing
llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
