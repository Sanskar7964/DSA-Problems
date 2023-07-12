def isBalanced(self, root):
     

        def height(root):
            if not root:
                return 0
            
            hl = height(root.left)
            if hl == -1:
                return -1
            hr = height(root.right)
            if hr == -1:
                return -1
            
            if abs(hr-hl)>0:
                return -1
            
            return 1+max(hl, hr)
        return height(root)!= False

