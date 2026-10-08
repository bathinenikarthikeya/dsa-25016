class ArrayBinaryTree:
    def __init__(self, capacity=100):
        self.tree = [None] * capacity
        self.capacity = capacity
 
    def insert(self, data):
        for i in range(self.capacity):
            if self.tree[i] is None:
                self.tree[i] = data
                return True
        return False 
 
    def search(self, key):
        for item in self.tree:
            if item == key:
                return True
        return False

    def _get_left_child(self, index):
        return 2 * index + 1
 
    def _get_right_child(self, index):
        return 2 * index + 2
 
    def preorder(self, index=0, result=None):
        if result is None: 
            result = []
        if index < self.capacity and self.tree[index] is not None:
            result.append(self.tree[index])
            self.preorder(self._get_left_child(index), result)
            self.preorder(self._get_right_child(index), result)
        return result
 
    def inorder(self, index=0, result=None):
        if result is None: 
            result = []
        if index < self.capacity and self.tree[index] is not None:
            self.inorder(self._get_left_child(index), result)
            result.append(self.tree[index])
            self.inorder(self._get_right_child(index), result)
        return result
 
    def postorder(self, index=0, result=None):
        if result is None: 
            result = []
        if index < self.capacity and self.tree[index] is not None:
            self.postorder(self._get_left_child(index), result)
            self.postorder(self._get_right_child(index), result)
            result.append(self.tree[index])
        return result
 
    def level_order(self):
        result = []
        for item in self.tree:
            if item is not None:
                result.append(item)
        return result
