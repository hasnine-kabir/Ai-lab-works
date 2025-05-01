from collections import deque

bfs_graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E'],
}

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes of graph.
    queue = deque([start])  # Initialize a queue with the starting node
    visited.add(start) # Mark the starting node as visited

    while queue:
        node=queue.popleft()  # Dequeue a node from the queue

        visited.add(node)
        print(node, end=" ") # Print the node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
bfs(bfs_graph, 'A')