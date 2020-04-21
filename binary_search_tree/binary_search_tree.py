from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        keep_going = True
        current = self
        while keep_going:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(value)
                    keep_going = False
            elif value >= current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree(value)
                    keep_going = False
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        keep_going = True
        current = self
        while keep_going:
            if current.value == target:
                return True
            elif target < current.value and current.left:
                current = current.left
            elif target >= current.value and current.right:
                current = current.right
            else:
                return False

                # Return the maximum value found in the tree

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
