def CombinationSum2(self, candidates: List[int], target: int)-> List[List[int]]:
    candidates.sort()

    res = []
    def Backtrack(curr, i, target):
        if target == 0:
            res.append(curr.copy())

        if target<=0:
            return
        
        prev = -1
        for i in range(candidates):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            Backtrack(curr, i+1, target-candidates[i])
            curr.pop()
            prev = candidates[i]

        Backtrack([], 0, target)
    return res