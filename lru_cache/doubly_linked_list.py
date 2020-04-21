"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        current = self.head
        rep = []
        if current:
            rep.append(current.value)
            while current.next:
                rep.append(current.value)
        return str(rep)
    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length = 1
        elif self.length == 1:
            self.head = ListNode(value, None, self.tail)
            self.tail.prev = self.head
            self.length += 1
        else:
            old_head = self.head
            self.head = ListNode(value, None, old_head)
            old_head.prev = self.head
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            old_head_value = self.head.value
            self.head, self.tail = None, None
            self.length = 0
            return old_head_value
        new_head = self.head.next
        old_head_value = self.head.value
        self.head.delete()
        self.head = new_head
        self.length -= 1
        return old_head_value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            old_tail_value = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return old_tail_value
        else:
            old_tail_value = self.tail.value
            new_tail = self.tail.prev
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
            return old_tail_value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if self.length <= 1:
            return None
        if self.head == node:
            return
        node.delete()
        self.head.prev = node
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.length <= 1:
            return
        if self.tail == node:
            return
        if self.head == node:
            self.head = self.head.next
        node.delete()
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length <= 1:
            self.head, self.tail = None, None
        if node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        keep_going = True
        max = self.head.value
        current = self.head
        while keep_going:
            if current.value > max:
                max = current.value
            if current.next:
                current = current.next
            else:
                keep_going = False
        return max
