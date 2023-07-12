# cycle in an undirected graph

def hasCycle(vertex, adj):
    visited = [False]*vertex

    for i in range(vertex):
        if not visited[i]:
            if dfs(adj, visited, i, -1):
                return True
            
    return False


def dfs(adj, visited, i, parent):
    visited[i] = True

    for neighbor in adj[i]:
        if not visited[neighbor]:
            if dfs(adj, visited, neighbor, i):

                return True
            elif neighbor != parent:
                return True
            


    return False