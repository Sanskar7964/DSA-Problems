#most stones removed

def removeStones(self, stones: List[List[int]]) -> int:
	
	def removeIsland(i,j):
		inIsland = [] 
		ind = 0 
		while ind < len(stones):
			x,y = stones[ind] 
			if x == i or y == j: 
				inIsland.append(stones.pop(ind)) 
			else:
				ind += 1
		for stone in inIsland: 
			removeIsland(*stone) 
	ans = len(stones) 
	while stones:
		removeIsland(*stones.pop()) 
		ans -= 1 
	return ans