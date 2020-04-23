import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


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
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        current_node = node
        while current_node:
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            current_node = queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        current_node = node
        # if there's something in the stack or the node is not empty
        while len(stack) or current_node is not None:
            # if the node is not empty, print it, push it on the stack, and go left
            if current_node is not None:
                stack.push(current_node)
                print(current_node.value)
                current_node = current_node.left
            # else, pop a node off of stack(go back a level), and go right
            else:
                current_node = stack.pop()
                current_node = current_node.right

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.post_order_dft(bst)
