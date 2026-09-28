# N-ary tree node
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

# Traverse the branches of an N-ary tree
def traverse_branch(root):
    # base case
    if root is None:
        return
    for child in root.children:
        print(f"visit branch: {root.val} -> {child.val}")
        traverse_branch(child)

# Graph node
class Vertex:
    def __init__(self, id=0, neighbors=None):
        self.id = id
        self.neighbors = neighbors if neighbors is not None else []

# Traverse the edges of a graph
# Need a 2D visited array to record visited edges,
# visited[u][v] indicates that edge u->v has been visited
def traverse_edges(s, visited):
    # base case
    if s is None:
        return
    for neighbor in s.neighbors:
        # if the edge has been visited, skip it
        if visited[s.id][neighbor.id]:
            continue
        # mark and visit the edge
        visited[s.id][neighbor.id] = True
        print(f"visit edge: {s.id} -> {neighbor.id}")
        traverse_edges(neighbor, visited)