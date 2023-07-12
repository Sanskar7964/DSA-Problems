def hasCycle(graph):

    path= set()
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        if node in path:
            return True
        
        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:

            if dfs(neighbor):
                return True
            
            path.remove(node)

            return False
        
    for node in graph:
        if dfs(node):
            return True
        
    return False
            

