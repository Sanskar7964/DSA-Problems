def isSameTree(self, p, q):

    if not p and q :
            return True
    if p.val != q.val:
            return False
    if not p or not q:
            return False
        
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)