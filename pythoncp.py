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

""" 
#path crossing: we can use co-ordinates in a hashSet and manipulate values according to our given string
class Solution:
    def PathCrossing(self, path: str)-> bool:
        x, y  = 0 , 0

        visit = set()
        visit.add("0 , 0")

        for c in path:
            if path[c] == "N":
                y+=1
            if path[c]== "S":
                y-=1
            if path[c] == "W":
                x-=1
            else:
                x+=1
            if f"{x},{y}" in visit:
                return True
            else:
                visit.add(f"{x},{y}")
        return False """



""" import heapq

class KthLargest:
    def __init__(self, nums: list, k : int):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while (len(self.minHeap)>k):
            heapq.heappop(self.minHeap)
    
    def add(self, val:int)->int:
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        if len(self.minHeap) < self.k or val> self.minHeap[0]:
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]
        
 """

""" class Solution:
    def charactersMakeEqual(self, words: list[str])-> bool:

        s = ''.join(words)
        count = Counter(s)

        for c in count:
            if count[c]%len(words)!=0:
                return False
        return True """

""" from collections import defaultdict
class Solution:
    def LargestSubstrTwoChar(self, s: str)-> int:
        indexing = {}
        #res = -1  

        for n, c in enumerate (s):
            if c not in indexing:
                indexing[c] = n
            else: 
                res = max(res, n - indexing[c]- 1)
        return res """

""" class Solution:
    def SetMismatch(self, nums:list[int])-> list[int]:
       
        res = []
        n  = len(nums) 
        count = Counter(nums)
        
        for c in range(1, n+1):
            if count[c]>1:
                 nums1 = c
            if count[c] == 0:
                nums2 = c
        return [nums1, nums2]

        #method 2
        res = [0,0]
        n = len(nums)

        for n in nums:
            n = abs(n)
            nums[n-1] = -nums[n-1]

            if nums[n-1]>0
            res[0] = n
        for i, c in enumerate(nums):
            if n>0 and i+1 != res[0]:
             res[1] = i+1
             return res

 """

""" class Solution:
    def UniqueChars(self, s: str)-> int:
        count = Counter(s)

        for i, n in enumerate(s):
            if count[n] == 1:
           
                return i
        return -1

 """
""" class Solution:
    def TimetoBuyTickets(self, tickets: list[int], k: int)-> int:
        
        res = 0

        for  i in range(len(tickets)):
            if i<=k:
                res += min(tickets[i], tickets[k])
            else: 
                res += min(tickets[i], tickets[k]-1 )

        return res
 """

  
""" class Solution:
    def ValidPalindrome(self, s:str)-> bool:
       #dummy = ''.join(c.lower() for c in s if c.isalnum())

        #return dummy == dummy[::-1] 

        dummy = ""

        for c in s:
            if c.isalnum():
                dummy+=c.lower()
            

        i, j = 0, len(dummy)-1

        while i<j:
            if dummy[i] != dummy[j]:
                return False
            i+=1
            j-=1
        return Tr
        
 """

# sliding window i = j cababac, abccba even length string = character count equal
#odd length string character count of 1 character > than the rest
 
""" class Solution:
   def PalindromicSubstrings(self, s: str)-> int:
       res1 = 0

       for i in range(len(s)):
           left, right = i, i
           while left>=0 and right<len(s) and s[left] == s[right]:
               res1+=1
               left -=1
               right +=1
        

     
           left, right = i, i+1
           while left>=0 and right<len(s) and s[left] == s[right]:
               res1+=1
               left -=1
               right +=1
           
       return res1
    """
""" 
class Solution:
    def encodeDecode(self, strs: list)-> list:

        def encode(self, strs):
            res  = ""
            for s in strs:
                res  = str(len(s))+'#'+s
            return res
        
        def decode(self, str):
            res = []
            i = 0

            while i<len(str):
                j = i
                while str[j] != '#':
                    j+=1
                    length = int(str[i:j])
                res.append(str[j+1:length+j+1])
                i = j+1+length
            return res
 """
""" class Solution:
    def KthDistinct(self, arr: list, k: int)-> str:
        count  = Counter(arr)
        distinct_count = 0
        
        for i in arr:
            if count[i] == 1:
                distinct_count +=1

                if distinct_count ==k:
                    return str(i)
        return ""

 """

""" class Solution:
    def TopKelements(self, nums: list, k:int)->list[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1+ count.get(n,0)

        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) ==k:
                    return res """
""" class Solution:
    def triangle(self, n:int)->list[int]:
        res = []

        for i in range(n):
            rows = [1]*(n+1)
            for j in range(1, i):
                rows[j] = rows[i-1][j-1]+rows[i-1][j]
            res.append(rows)

        print(' '.join(map(str, rows)).center(n * 2))

    
    n=5
    triangle(n) """

""" class NumArray:

    def __init__(self, nums:list[int]):
        self.prefix = []
        curr = 0

        for i in  range(nums):
            curr += nums[i]
            self.prefix.append(curr)

    def sumRange(self, left:int, right:int)-> int:
        sum  = self.prefix[right] - self.prefix[left] if left>0 else 0

        return sum """

#xyzy

""" class Solution:
    def PermutationString(self, s1: str, s2: str)-> bool:
        new_substring = ""
        n = len(s1)

        for i in range(n):
            if n == 1 and s1 in  s2:
                return True

            elif n ==2:
                new_substring += s1[0]
                new_substring += s1[1]
                if new_substring in s2:
                    return True
            else:
                new_substring += s1[0:i] + s1[i+1: n]
                new_substring += "s1[i]"

                if new_substring in s2:
                    return True
        return False

         """
""" class Solution:
    def ReorganizeString(self, s: str)-> str:
        count = {}

        for i in range(s):
            count[s[i]] = 1 + count.get(i, 0)
        
        if len(s)%2 != 0:
            if max(count.values()) - sum()

    
             """
class Solution:
    def LemonadeChange(self, bills: list[int])-> bool:
        cnt5 = 0
        cnt10 = 0

        for b in bills:
            if b ==5:
                cnt5 +=1
            if b == 10:
                cnt10 +=1

            change = b-5
            if change == 5:
                if cnt5>0:
                    cnt5 -=1
                
            if change == 15:
                if  cnt5 > 0 and cnt10 > 0:
                    cnt10 -=1
                    cnt5 -=1
                elif cnt5 >=3:
                    cnt5 -= 3
                else:
                    return False
        return True
    
