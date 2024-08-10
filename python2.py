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
      
