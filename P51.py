#good nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxValue):
                if not node:
                   return 0

                res = 1 if node.val>maxValue else 0 
                maxValue = max(node.val, maxValue)
                res += dfs(maxValue, node.left)
                res += dfs(maxValue, node.right)
                return res

        return dfs(root, root.val)