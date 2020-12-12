class Node:
"""Binary tree node."""
    def __init__(self, data=None):
        self.left = left
        self.data = data
        self.right = right
    
    def __iter__(self):
        """In-order traversal of the items."""
        if self.left:
            yield from self.left
        if self.data:
            yield self.data
        if self.right:
            yield from self.right
    
    def insert(self, data):
        if not self.data:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    def search(self, val):
        if val == self.data:
            return self
        elif val < self.data:
            if self.left is None:
                raise KeyError
            else:
                self.left.search(val)
        elif val > self.data:
            if self.right is None:
                raise KeyError
            else:
                self.right.search(val)
        
    
