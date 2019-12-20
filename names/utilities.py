

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = None
        parent = self
        if parent.value is None:
            parent.value = value
            return
        node = BinarySearchTree(value)
        while True:
            if value < parent.value:
                current = parent.left
                if not current:
                    parent.left = node
                    return
            elif value == parent.value: return value
            else:
                current = parent.right
                if not current:
                    parent.right = node
                    return
            parent = current


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = None
        parent = self
        if parent.value is None: return False
        while True:
            if target < parent.value:
                current = parent.left
                if not current: return False
            elif target == parent.value: return True
            else:
                current = parent.right
                if not current: return False
            parent = current


    # Return the maximum value found in the tree
    def get_max(self, node=None, recursive=False):
        if not node and recursive: return False
        if not node: node = self
        if not node.left and not node.right: return node.value
        elif not node.right: return max(node.value, node.get_max(node.left, True))
        elif not node.left: return max(node.value, node.get_max(node.right, True))
        return max(node.value, node.get_max(node.left, True), node.get_max(node.right, True))

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, node=None, recursive=False):
        if not cb: return
        if not node and recursive: return
        if not node: node = self
        if node.value: cb(node.value)
        self.for_each(cb, node.left, True)
        self.for_each(cb, node.right, True)