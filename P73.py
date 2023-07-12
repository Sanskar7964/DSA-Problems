#Count paths

def countPaths(self, n, roads):
       
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[v].append((u,t))
            graph[u].append((v,t))

        dist = [float('inf')]*n
        dist[0] = 0

        ways = [0]*n
        ways[0] = 1

        pq = [(0,0)]

        while pq:
            oldDist, u = heappop(pq)
            for v, t in graph[u]:
                newDist = oldDist + t
                if newDist < dist[v]:
                    heappush(pq, (newDist, v))
                    dist[v] = newDist
                    ways[v] = ways[u]
                elif newDist == dist[v]:

                    ways[v] += ways[u]

        mod = 10**9+7
        return ways[-1]%mod
                

        