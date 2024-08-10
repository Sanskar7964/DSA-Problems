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
