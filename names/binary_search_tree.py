from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"BinaryTree({self.left}, {self.value}, {self.right})"

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:  # if value is smaller than node
            if self.left:  # look left
                self.left.insert(value)  # if node, repeat
            else:
                # if no node, make one a new leaf with value
                self.left = BinarySearchTree(value)
        # if value is greater or equal
        else:
            if self.right is not None:  # look right
                self.right.insert(value)
            else:
                # if no node, make a new leaf with value
                self.right = BinarySearchTree(value)

    def contains_recursively(self, target):
        if self.value == target:
            return True
        else:
            if self.value < target:
                return False if self.right is None else self.right.contains_recursively(target)
            else:
                return False if self.left is None else self.right.contains_recursively(target)

    def contains_iteratively(self, target):
        current = self
        while current:
            if current.value == target:
                return True
            elif current.value < target:
                current = current.right
            else:
                current = current.left
        return False

    def get_max_iterative(self):
        current = self
        highest = current.value
        while current.right is not None:
            current = current.right
        return current.value if current is not None else highest

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return max(self.value, self.right.get_max())

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # breadth-first traversal
    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

    def for_each_before(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def for_each_middle(self, cb):
        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

    def for_each_after(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        cb(self.value)

    # def for_each(self, cb):
    #     cb(self.value)
    #     current = self
    #     while current.left is not None:
    #         current = current.left
    #         cb(current.value)
    #         print(f'value {current.value}')
    #         while current.right is not None:
    #             current = current.right
    #             cb(current.value)
    #             print(f'value {current.value}')
    #     current = self
    #     while current.right is not None:
    #         current = current.right
    #         cb(current.value)
    #         print(f'value {current.value}')
    #         while current.left is not None:
    #             current = current.left
    #             cb(current.value)
    #             print(f'value {current.value}')

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print_recursively(self, node):
        if self.left:
            self.left.in_order_print_recursively(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print_recursively(self.right)

    # this wont work because it needs control flow to not revsit
    def in_order_print(self, node):
        stack = Stack()
        stack.push(node)
        current = node
        while stack.size > 0:
            while current.left:
                current = current.left
                stack.push(current)
            current = stack.pop()
            print(current.value)
            while current.right:
                current = current.right
                stack.push(current)

    # def in_order_print(self, node):
    #     stack = Stack()
    #     stack.push(node)
    #     while stack.size > 0:
    #         current = stack.pop()
    #         if current.left is not None:
    #             stack.push(current.left)
    #         if current.right is not None:
    #             stack.push(current.right)
    #         print(current.value)

        # initialize a stack
        # push root to stack
        # while stack not empty
        # pop top item out of stack into temp
        # DO THE THING!!!!!!
        # if temp has right right put into stack
        # if temp has left left put into stack

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current = queue.dequeue()
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current = stack.pop()
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

        # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)
