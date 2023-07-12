def mintoconnect(self, points: List[List[int]]) -> int:
    N = len(points)

    graph = defaultdict(list)

    for u, v, t in points:
        graph[v].append((u,t))
        graph[u].append((v,t))

    res = 0 
    visit =set()
    minH = [[0,0]]
    while len(visit)<N:
        cost, i =  heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neicost, nei in graph[i]:
            if nei not in visit:
                heapq.heappush(minH, [neicost, nei])

    return res