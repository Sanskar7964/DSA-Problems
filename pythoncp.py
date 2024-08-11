""" def minCost2(stones, k):
    
    n = len(stones)
    memo = [-1]*n
    memo[0] = 0
    memo[1] = abs(stones[1] - stones[0])
    return helper(stones, n-1, k, memo)

def helper(stones, index, k, memo):
    if memo[index] != -1:
        return memo[index]
    
    cost = float('inf')
    for i in range(1, k-1):
        if index -1>=0:
    
            price = helper(stones, index-1,k, memo) +abs(stones[index] - stones[index-1])


    memo[index] = min(price)
    return memo[index]
  """

""" class solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l = r = i

            while l>= 0 and r<len(s) and s[l] == s[r]:
                if 
                res += 1
                l -= 1
                r += 1


            l = i
            r = i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1


        return res
     """
""" class solution:
    def countSubstrings(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l = r = i

            while l>= 0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                   
                 res = s[l:r+1]
                 l -= 1
                 r += 1


            l = i
            r = i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                   
                 res = s[l:r+1]
                 l -= 1
                 r += 1


        return res """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
""" 
class solution:
    def maxDepth(self, root:Treenode) -> int:
        if not root:
            return 0
        
        queue = deque([root])

        depth = 0

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
        
        return depth
 """
""" def maxDepth(self, node: TreeNode) -> int:
    if not node: 
        return 0
    

    left_depth = self.maxDepth(node.left)
    right_depth = self.maxDepth(node.right)
    depth = max(left_depth, right_depth)+1

    return depth
 """
""" 
class solution:
    def invertTree(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        node.left, node.right = node.right, node.left

        self.invertTree(node.left)
        self.invertTree(node.right)

        return node
    
     """



""" class solution:
    def LOT(self, node: TreeNode)-> list[list[int]]:
        if not node:
            return []
        
        res = []
        queue = deque([node])

        while queue:
            queue.popleft()
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)


                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res

 """

""" [2,4,5,7]
    [7,5,4,2] """


""" class Solution:
  def twosum(self, nums:list, target: int)-> list:
     res = []
     map = {}
     for i, num in enumerate(nums):
    
        var = target - num
        if var in map:
           res.append([map[var], i])
           map[num] = i
        
     return res
     
 """