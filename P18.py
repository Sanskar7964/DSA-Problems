def countPartitions(n: int, target: int, arr: List[int], sum:int) -> int:
        n = len(arr)

        for i in enumerate(arr):
          sum += i
        if(((sum-target)%2 ==1 or (target>sum) )):
             return 0
        
        p1 = (sum-target)/2

        

