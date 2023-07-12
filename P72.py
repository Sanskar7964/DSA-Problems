class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        
        rows = len(heights)
        cols = len(heights[0])

        heap = [(0,0,0)]
        visit = set()
        directions = [[0,1], [1,0], [-1, 0], [0, -1]]
        ans = 0
        while heap: 
            r, c, diff = heappop(heap)
            ans = max(diff, ans)
            
            if r == rows-1 and c == cols-1:
                return ans
            visit.add((r, c))
            for dr, dc in directions:
                newRow = r+dr
                newCol = c+dc
                if((newRow, newCol) not in visit and 0<newCol<cols and 0<newRow<rows):
                    new_diff = abs(heights[r][c] - heights[newRow][newCol])
                    heappush(heap, (newRow, newCol, new_diff))
                    

        return -1