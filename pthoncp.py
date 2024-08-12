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

""" class Solution:

    def StockPrice(self, prices: list)-> int:
        if not prices:
            return 0
        min_value = prices[0]
        max_price = 0
        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]

            else:
                max_price = max(max_price, prices[i]-min_value )
        return max_price """


""" from collections import Counter
class Solution:
    def ContainsDuplicate(self, nums: list)-> bool:
         visit = set()
        for num in nums:
            if num in visit:
                return True
            visit.add(num)

            return False 

       //method 2: using a frequency map
       count = counter(nums)

       for num in nums:
           if count[num]>1:
            return True
           
       return False 
"""


""" class Solution:
    def MaxSubarray(self, nums: list)-> int:
        if not nums:
            return 0 
        
        max_value = max_global = nums[0]

        for num in nums[1:]:
            max_value = max(num, max_value+num )

            if max_value>max_global:
                max_global = max_value

        return max_global """
    
""" class Solution:
    def MaxProduct(self, nums:list)->int:
        res =  max(nums)
        if not nums:
            return 0 
        
        curr_max= curr_min   = 1

        for n in nums:
            if n ==0:
                curr_max = curr_min = 1
                continue
            curr_max = max(curr_max*n, curr_min*n, n)
            curr_min = min(curr_min*n, curr_max*n, n)

            res = max(curr_max, res)
        return res

 """
""" 
class Solution:
    def Permute(self, nums:list)-> list:
        if not nums:
            return [[]]
        res = 
        for i, num in enumerate(nums):
            perm = nums[:i] + nums[i+1:]
            for i in self.permute(perm):
                res.append([num]+i)

        return res
 """


""" 
#uses binary search to find the min element in a rotated sorted array.

class Solution:
    def findMinElement(self, nums:list)-> int:
        left, right = 0, len(nums)-1
        while  left<right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1

            else:
                right = mid
        return nums[left]
                 """

""" 
#search for a specific target value in a sorted rotated array
class Solution:
    def findMinElement(self, nums:list, target:int)-> int:
        left, right = 0, len(nums)-1
        
        while  left<right:
        
          mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
          
            if nums[left] <= nums[mid]:  
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1
                else: 
                    left = mid + 1
            else:  
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1
                else:  
                    right = mid - 1
        return -1 """

""" 
# finding three sum without duplicates
def ThreeSum(self, nums:list)-> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:

            continue
        left, right = i+1, len(nums)-1
        while left< right:
            sum = nums[i] + nums[left]+ nums[right]

            if sum> 0:
                right -=1
            elif sum<0:
                left +=1
            else:
                result.append((nums[i], nums[left], nums[right]))

            while left < right and nums[left] == nums[left+1]:
                left +=1
            while left< right and nums[right] == nums[right-1]:
                right -=1
            
            left+=1 
            right -=1

    return result """


""" 
# two sum using bit manipulation

class Solution:
    def twoSumBitsum(self, a:int ,b: int) -> int:
        while b != 0:
            sum = a^b
            carry = (a&b)<<1

            a = sum
            b = carry
        return a

 """
""" 
# count of hamming number 
class Solution:
    def numOfBits(self, n: int)-> int:
        count = 0
        binary_rep = bin(n)
        binary_rep = binary_rep.replace("0b", "")
        for c in binary_rep:
            if c == '1':
                count +=1

        return count """

""" class Solution:
    def CountOfOne(self, n: int)-> list:
        res = []
        for i in range(n):
            binary_rep = bin(i).count('1')
            res.append(binary_rep)

        return res
 """

""" class Solution:
    def ClimbStairs(self, n: int) -> int:
        if n == 1:
         return 1
        if n == 2:
            return 2
        ways= [0]*(n+1)
        ways[1] =1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-1]+ ways[i-2]

        return ways[n] """

""" 
#minimum deletion needed to make a string balanced. e,g aaababbab - 2(remove 2 a's)

class Solution:
    def minimumDeletions(self,s :str)-> int:
        a_count =  0
        for i in range(len(s)):
            a_count[i] = a_count[i+1]
            a_count[i]+=1 if s[i+1] == "a" else 0

        b_count = 0
        res = len(s)
        for i, c in enumerate (s):
            res = min(res, a_count[i]+b_count)
            if c == "b":
                b_count += 1
        return res
 """


""" 
#Coin change

class Solution:
    def MinimumCoins(self, coins: list, amount: int) -> int:
        dp = [amount+1]*(amount+1)

        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c>0:
                   dp[i] = min(dp[c], 1+dp[i-c])

        return dp[amount] if dp[amount ]!= amount+1 else -1 """
""" 
#Longest increasing subsequence// uses two pointers 
class Solution:
    def longestIncraesingSubsequence(self, nums: list)-> int:
        dp = [1]*len(nums)
        if not nums:
            return 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)-1):
                if nums[i]<nums[j]:
                  dp[i] = max(dp[i], dp[j]+1)

        return max(dp) """

""" class Solution:
    def LCS( self, text1: str, text2:str)-> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range((m-1), -1, -1):
            for j in range((n-1), -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] =1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]
                 """

""" 
#using two pointers and iterating through the word string to check segment equality. 
# Only the starting and ending the character of words have to be marked true
class Solution:
    def WordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n =  len(s)
        dp = [False]*(n+1)
        dp[0] =  0

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                break
        return dp[n] """

""" class Solution:
    def NumberofCitizens(details: list)-> int:
        count = 0
        if not details:
            return None
        for c in details:
            new_segment = c[11:13]
            if new_segment>'60':
                count +=1       
        return count
 """

""" class Solution:
    def CombinationSum(self, candidates: list, target: int)-> int:
        res = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i>= len(candidates) or total>target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1,curr, total)

        dfs(0,[], 0)

        return res """

""" class Solution:
    def HouseRobber(self, nums:list)-> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums))
             dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1] """

"""
# we will require a helper function to callback for :-1, 1: segments
#same code as houserobber 1
 class Solution:
    def HouseRobber2(self, nums:list)-> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
         
         def helper(nums):
         
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]

            for i in range(2, len(nums)):
                if i == nums-1 and i-2 == 0:
                    return dp[i-1]
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])

            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))
         """



""" class Solution:
    def decodeWays(self, s:str)-> int:
        dp = [0]*(len(s)+1)

        dp[0] = 1
        dp[1] = 1
        if not s:
            return 0
        for i  in range(2, len(s)+1):
            c = int(s[i-1:i])
            if 1<=c <= 9:
                dp[i]+=dp[i-1]

            c1 = int(s[i-2:i])
            if 10<=c1 <= 26:
                dp[i]+=dp[i-2]   

        return dp[len(s)]
 """
""" class Solution:
    def UniquePaths(self, m:int, n:int)-> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                dp[i][j] =  dp[i+1][j]+dp[i][j+1]
        return dp[0][0] """

""" #intuition is that we'll iterate over the entire loop and keep a sum of i+nums to check if we can reach to the end 
class Solution:
    def JumpGame(self, nums:list)-> bool:
        if not nums:
            return True
        for i in range(nums-1,-1,-1):
            goal = len(nums)-1
            if i+nums[i]>= goal:
                goal = i
        return True if goal == 0 else False """


class ListNode(self, val = 0, next=None):
    self.val = val
    self.next = next

""" class Solution:
    def reverselist (self, head:ListNode)-> ListNode:
        prev = None
        curr  = head
        while curr:
            next_node = head.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
 """
""" class Solution:
    def Cycle(self, head:ListNode)-> bool:
        if not head or head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False """


""" 
# to count the number of prime numbers between a given range
class Solution:
    def NumOfPrimeNumbers(self, nums: int)-> list:
        nums = range(1,1000)
        
        def is_Prime(self, n:int)-> bool

        for x in range(2, floor(sqrt(n))):
            if (n%x) == 0:
                return False
           
        return True

    primes = filter(list(is_Prime, nums))
    print(primes) """

""" class ListNode(self, val = 0, next=None):
    self.val = val
    self.next = next

class Solution:
    def MergeLists(self, l1:ListNode , l2: ListNode)-> ListNode:
        dummy  = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val> l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr= curr.next

        if l1:
            curr.next = l1
            l1= l1.next
          

        if l2:
            curr.next = l2
            l2= l2.next
          
            
        return dummy.next """

""" 
#logic is that you have to keep two pointers and iterate them with 
# a window of k. first pointer would point to end while send would be 
# behind the require node k
class ListNode(self, val=0, next=None):
    self.val = val 
    self.next = next

class Solution:
    def RemoventhNode(self, head: ListNode, n: int)-> ListNode:
        if not head or head.next:
            return None
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        

        for i in range(n+1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
 """
""" class ListNode(self, val= 0, next= None):
    self.val = val 
    self.next = next

class Solution:
    def ReorderList(self, head: ListNode)-> ListNode:
        if not head:
            return None
        
        def Middle(head):
            fast=  head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow= slow.next 
            return slow
        def reverse(head):
            
            curr = head
            prev = None

            while curr:
                next_node = head.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        def mergeList(l1,l2):
            while l2:
                tmp1, tmp2 = l1.next, l2.next
                l1.next = l2
                l2.next = tmp1
                l1 = tmp1
                l2 = tmp2

        mid = Middle(head)
        second_half = reverse(mid.next)
        mid.next = None
        mergeList(head, second_half)

 """
""" class Solution:
    def LS(self, s: str)-> int:
        
        char_set = set()
        left = 0 
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            max_length = max(max_length, right-left+1)

        return max_length """

""" class Solution:
    def LRCR(self, s: str, k: int)-> int:
        left = 0
        count = defaultdict(int)
        max_frequency= 0

        for right in range (len(s)):
            count[s[right]] += 1
    
            window_length  = right-left+1
            max_frequency = max(max_frequency, count[s[right]])

            if window_length- max_frequency>k:
                count[s[left]] -=1
                left+=1
         
            res=  max(res, right-left+1)

        return res

 """
""" 
class Solution:
    def validAnagram(self, s:str, t:str)-> bool:

        if len(s) != len(t):
            return False
        
        count1  = Counter(s)
        count2  = Counter(t)

        if count1 == count2:
            return True
        else: False
        
       """
""" class Solution:
    def groupAnagrams(self, strs: list[str])-> list[list]:
         res = defaultdict(list)
         
         for s in strs:
             count= [0]*26

             for c in s:
                 count[ord(c)-ord("a")] += 1

             res[tuple[count]].append(s)
         return res.values()
    
 """
""" class Solution:
    def ValidBrackets(self, s: str)-> bool:
        stack = []
        mapping = {")" : "(",  "]":"[", "}":"{"}


        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]: # case for closing parenthesis
                    stack.pop()
                else:
                    return False
            else:
                stack.append() # case for opening parenthesis

        return True if not stack else False
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
class Solution:
    def triangle(self, n:int)->list[int]:
        res = []

        for i in range(n):
            rows = [1]*(n+1)
            for j in range(1, i):
                rows[j] = rows[i-1][j-1]+rows[i-1][j]
            res.append(rows)

        print(' '.join(map(str, rows)).center(n * 2))

    
    n=5
    triangle(n)
