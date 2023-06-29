def isBalancd(self, root):

    return self.height(root)!= -1

    def height(self, root):
        if not root:
            return 0
        
        hl = self.height(root.left)
        if hl == -1:
            return -1
        hr = self.height(root.right)
        if hr == -1:
            return -1
        
        if abs(hr-hl)>0:
            return -1
        
        return 1+max(hl, hr)

    return height(self, root)!= False