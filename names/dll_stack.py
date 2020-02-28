from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # a lot of insertion at the head and then
        self.storage = DoublyLinkedList()

    def __repr__(self):
        return self.storage.__repr__()

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
