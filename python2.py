from collections import Counter
""" class Solution:
    def DisappearedNumbers(self, nums:list)->list:
        
        res = []
        arr = set(nums)

        if not nums:
            return []

        for i in range(1, len(nums)+1):
            if i not in arr:
                res.append(i)
        return res

 """

""" def BallonsMatch(self, text: str)->int:
    count1, count2  = Counter(str), Counter("balloon")

    res = float('inf')

    for c in count2:
        res = min(res ,(count1[c]//count2[c]))

    return res """

""" 
def WordPattern(self, s: str, pattern: str)-> bool:
    words = s.split()
    char_to_word = {}
    word_to_char = {}

    for c, n in zip(pattern, words):
        if c in char_to_word and char_to_word[c] != n:
            return False
        else:
            char_to_word[c] = n

        if n in word_to_char and word_to_char[n] != c:
            return False
        else:
            word_to_char[n] = c
    return True

 """
      """
class ListNode:
    def __init__(self, key = 1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode for i in range(1000)]

    def hash(self, key):
        return key%len(self.map)

    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return 
            curr = curr.next
        curr.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)]
        while curr:
            if curr.key ==key:
                return curr.val
            curr = curr.next
        return -1  
        
    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]

        while curr and curr.next:
            if curr.next.key ==key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return -1 """


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
""" 
class Solution:
    def SpecialArrayWithX(self, nums: list[int])-> int:
        n = len(nums)
        res = [1]*(n)
        nums.sort()

        for i in range(n):
            res[i] = n-i

        for j in range(n):
            if res[j] <= nums[j]:
                return res[j]
        return -1

 """

""" #top k most frequent elements // using bucket sort
# way of sorting decrementing freq // sorted_items = sorted(mapping.items(), key: lambda item: items[1], reverse = True)
class Solution:
    def TopKmostElement(self, nums: list[int], k: int)-> list[int]:
        mapping = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            mapping[i] = 1+ mapping.get(i,0)
        
        for n, c in mapping.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res """

