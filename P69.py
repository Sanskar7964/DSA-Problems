#courseSchedule 1

def canFinishCourses(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)


    visitSet = set()

    def dfs(course):
        if course in visitSet:
            return False
        if graph[course] == []:
            return True
        
        visitSet.add(course)

        for nei in (graph):
            if not dfs(nei):
                return False

        visitSet.remove(course)
        graph[course] ==  []
        return True

    for node in range(numCourses):
        if not dfs(node):
            return False
    return True

 