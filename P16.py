# min difference partition

def minDiffernce(self, arr, n):
    
    total_sum = sum(arr)
    dp = [[False for j in range((total_sum//2)+1)]for i in range(n+1)]

    for i in range(len(dp)):
      dp[i][0] = True
      
    for i in range(1, len(dp)):
      for j in range(1,len(dp[0])):
          if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
          else:
             dp[i][j] = dp[i-1][j]
                    
    min_diff = float('inf')
    for i in range(len(dp[0])-1, -1, -1):
      if dp[-1][i]:
         min_diff = min(min_diff, abs(total_sum-(2*i)))
         return min_diff