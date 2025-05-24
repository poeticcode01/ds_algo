class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def buildBST(self, root):
        if root is None:
            return

        # Reverse in-order traversal: right → root → left
        self.buildBST(root.right)

        # Set right child to previously visited node
        root.right = self.prev
        self.prev = root

        # Set left child to None (flatten)
        self.buildBST(root.left)
        root.left = None

    def flattenBST(self, root):
        self.prev = None
        self.buildBST(root)
        return self.prev  # New head of the flattened list