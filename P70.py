#Find the eeventual safe states

def eventualSafeNodes(self, graph: list[list[int]])-> list[int]:
    n = len(graph)
    map = {}

    def dfs(i):
        if i in map:
            return map[i] 
        
        map[i] = False

        for nei in graph[i]:
            if not dfs(nei):
                return map[i]
            map[i] = True

            return map[nei]
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)

        return res