class Tree:

    def __init__(self, root):
        self.root = root

    def in_order(self):
        if self.root is None:
            return
        if self.root.left is not None:
            Tree(self.root.left).in_order()
        print(self.root.value)
        if self.root.right is not None:
            Tree(self.root.right).in_order()