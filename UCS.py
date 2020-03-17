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
