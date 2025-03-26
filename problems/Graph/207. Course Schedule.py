

def courseSchedule(N, pre):
    
    # Create the adjacency list
    adj = [[] for _ in range(N)]
    for i in pre:
        adj[i[1]].append(i[0])

    # Lets use topological sort to solve this problem
    indegree = [0 for _ in range(N)]
    for i in range(N):
        for j in adj[i]:
            indegree[j] += 1

    queue = []
    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.pop(0)
        for i in adj[node]:
            indegree[i]-=1
            if(indegree[i]==0):
                queue.append(i)
    
    return sum(indegree)==0

N=4
prerequisites=[[1,0],[2,1],[3,2]]

print(courseSchedule(N,prerequisites)) #True