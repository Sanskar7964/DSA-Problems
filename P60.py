#Graph striver 

def printGraph(V, adj):
    new_adj = [[]for _ in range(V)]

    for i in range(V):
        new_adj[i].append(i)


        for node in adj[i]:
            new_adj.append(node)

    return new_adj
