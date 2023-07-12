def maxDepth(self, root):
     
        if not root:
            return 0

        res = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return res