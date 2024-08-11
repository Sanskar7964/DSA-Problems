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
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right"""
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

""" class Solution:
    def MonotonicArray(self, nums: list)-> bool:
        increasing = True
        decreasing  = True

        if len(nums) < 2:
            return True

        for i in range(len(nums)):
            if nums[i] > nums[i-1]:
                increasing = False
               
            if nums[i] < nums[i-1]:
                decreasing = False
                

            if not increasing and not decreasing:
                return False
        return increasing or decreasing """


""" class Solution:
# keep a counter and using Ncr or just count sum.
    def numberofgoodpairs(self, nums:list)-> int:
        #using a counter
        cnt = Counter(nums)
        count = {}
        ans = 0
        for n, c in cnt:
            ans += c*(c-1)//2
        return ans """
""" 
    #using a hash map
        for i in range(len(nums)):
            ans += count[i]
            count[i]+=1
            
        return ans """

""" 
#pascals triangle function to get the desired row.
class Solution:
    def pascalsTriangle(self, rowIndex:int)-> list:
        res = [[1]]
        for i in range(rowIndex+1):
            triangle =[1]*(i+1)
            for j in range(1, i):
                triangle[j] = res[i-1][j] + res[i-1][j+1]
            res.append(triangle)
        return res[rowIndex]

 """ 
""" class Solution:
    def goodstrings(self, words: list[str], chars: str)-> int:
        str_count = Counter(chars)
        res = 0

        if not words:
            return -1

        for c in range(len(words)):
            count = Counter(c)
            if count[c] == str_count[c]:
                res += len(count)
            count[c] = 0
        return res """

""" class Solution:
    def Largestthreedigit(self, num: str)-> str:
        count_char = Counter(num)
        num = ''.join(list(sorted(num)))
        res = ""
        if not num:
            return res

        for c in range(len(num)-1, 0, -1):
            if count_char[c] == 3:
                res = "c"+"c"+"c"
                count_char[c] = 0
                return res
                
        return ""
             """
""" 
#destination city 
class Solution:
    def DestinationCity(self, paths: list[list[str]])-> str:
        lst = set()

        for n,c in paths:
            lst.add[n]

        for n, c in paths:
            if c not in set:
                return c """

""" #max score after splitting the string
class Solution:
    def maxScore(self, s: str)-> int:
        n = len(s)
        res = 0
        for i in range(1, n):
            left = s[:i]
            right = s[i:]

            count_0s  = left.count('0')
            count_1s = right.count('1')
            res = max(res, count_0s+count_1s)

        return res """
