def prim(graph):
    
    V = len(graph)
    pq = []
    
    key = [float('inf')] * V
    
    parent = [None] * V
    
    visited = [False] * V

    
    source = 0
    key[source] = 0
    heapq.heappush(pq, (0, source))

    
    while pq:
        
        weight, u = heapq.heappop(pq)
        visited[u] = True

        
        for v, w in graph[u]:
            
            if not visited[v] and w < key[v]:
                
                key[v] = w
                
                parent[v] = u
                
                heapq.heappush(pq, (w, v))

   
    mstWeight = sum(key)

    return mstWeight
