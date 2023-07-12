#graphBipartite
def isgraphBipartite(graph):
    colors = {}

    def dfs(node, color):
        colors[node] = color

        for nei in graph[node]:
            if nei not in colors:
                if not dfs(nei, color-1):
                    return False
                
                elif colors[nei] == color:
                    return False
                
        return True
    
    for node in graph:
        if node not in colors:
            if not dfs(node, 0):
                return False
            

    return True
