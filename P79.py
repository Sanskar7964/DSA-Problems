def preorderTraversal(self, root)-> List[int]:
    if not root:
        return
    a = [root]
    ans = []

    while a:
        node = a.pop
        ans.append(node.val)

        if node.right:
            ans.append(node.right)

        if node.left:
            ans.append(node.left)

    return ans