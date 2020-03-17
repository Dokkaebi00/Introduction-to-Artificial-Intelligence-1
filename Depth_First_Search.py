# %% [markdown]
# # Create Graph
# We have to create graph like this: 
# ![alt text](https://www.educative.io/api/edpresso/shot/5410617873661952/image/6437799702036480 "Graph")


# %%
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# %% [markdown]
# # Write DFS Algorithm code
# %%
visited = [] # Array to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, 'A')
        

