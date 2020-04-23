class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)
        # print(self.storage)

    def delete(self):
        if self.get_size():
            max = self.storage.pop(0)
            if self.get_size() < 1:
                return max
            else:
                self._sift_down(0)
                self._sift_down(1)
                return max
        return None

    def get_max(self):
        return self.storage[0] if self.get_size() else None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # find parent element
        parent_index = (index-1)//2
        # while parent is smaller than new node, swap them, set new parent
        while self.storage[index] > self.storage[parent_index] and index != 0:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            index = parent_index
            parent_index = (index-1)//2

    def _sift_down(self, index):
        # Func to find index of the larger child
        def find_larger_child_index(i):
            size = self.get_size() - 1
            first_child = None
            second_child = None
            if index >= size:
                return None
            if size >= i*2 + 1:
                first_child = self.storage[i*2 + 1]
            else:
                return None
            if size >= i*2 + 2:
                second_child = self.storage[i*2 + 2]
            else:
                return i*2 + 1
            return i*2+1 if first_child > second_child else i*2+2

        larger_child_i = find_larger_child_index(index)
        # compare element to it's largest child, swap them if the child is bigger.
        while larger_child_i is not None and self.storage[larger_child_i] > self.storage[index]:
            self.storage[larger_child_i], self.storage[index] = self.storage[index], self.storage[larger_child_i]
            index = larger_child_i
            larger_child_i = find_larger_child_index(index)
