class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.value}, {self.next_node})"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def __repr__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.value) + ' '
            current = current.next_node
        return s

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        if self.head is None:
            return None
        current = self.head
        new = self.head.next_node
        self.head.next_node = None
        while new is not None:
            prev = current
            current = new
            new = current.next_node
            current.next_node = prev
        self.head = current
        return self.head

    def reverse_list_recursively(self, node, prev=None):
        # base case
        if node is None:
            self.head = prev
            return prev

        # actually need to traverse
        reverse = self.reverse_list_recursively(node.next, node)
        node.next = prev

        # return tail (which is new head)
        return reverse
