from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None  # what's going to be overwritten
        self.storage = DoublyLinkedList()

    def __repr__(self):
        return self.storage.__repr__()

    def append(self, item):
        # if empty, set the current to the head
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if less than capcacity, link the tail to head after adding
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
        # otherwise, overwrite the oldest, and move the oldest to next item
        # since tail is linked to head, this works fine
        else:
            self.current.value = item
            self.current = self.current.next

            # if at capacity, remove the oldest (head), add to tail
            # you don't replace new nodes, you change the value

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not self.storage.tail:
            list_buffer_contents.append(current.value)
            current = current.next

        list_buffer_contents.append(self.storage.tail.value)

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
