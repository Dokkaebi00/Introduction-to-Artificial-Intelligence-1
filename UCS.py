# %% [markdown]
# # Create Graph
# We have to create graph like this: 
# ![alt text](UCS_Graph.png.jpg "Graph")

# %%
graph = {
    'A' : [{'B': 5, 'D': 3}],
    'B' : [{'C': 1}],
    'C' : [{'E': 6, 'G': 8}],
    'D' : [{'E': 2, 'F': 2}],
    'E' : [{'B': 4}],
    'F' : [{'G': 3}],
    'G' : [{'E': 4}]
}

def ucs(graph, node, destination):
    visited = [] # Array to keep track of visited nodes.
    queue = [] # Initialize a queue
    cost = 0 # Initialize cost
    # create initial node {'A' : 0}
    visited.append(node)
    queue.append(node)
    
    while queue:
        # So sanh node vs destination, if == print destionation
        # so sanh tat cost all queue 
        # Neu tat ca bang nhau => Result = queue.pop(0)
        # else Result = queue.pop(phan tu be nhat)
        print(Result, end=" ")

        # for Neighbour in graph[Result][0]:
        #     if Neighbour not in visited:
        #         visited.append(Neighbour) #Cost = CostOld + CostNew
        #         queue.append(Neighbour) #Cost = CostOld + CostNew

bfs(graph, 'A')

