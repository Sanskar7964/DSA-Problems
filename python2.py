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