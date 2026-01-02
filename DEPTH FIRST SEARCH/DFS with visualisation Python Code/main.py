def dfs_trace(graph, start):

    #initialising visited to keep a track of visited nodes
    visited = set()

    #initialising a stack with the start node
    stack = [start]

    #keeping a trace of the order of nodes visited
    order = []

    #while there are nodes to visit in the stack
    while stack:

        #pop a node from the stack
        node = stack.pop()

        print(f"Stack after popping: {stack}")

        #print the current node being visited
        print(f"Visiting node: {node}")

        #if the node has not been visited
        if node not in visited:
            visited.add(node)
            #adding the node to the order of visited nodes

            order.append(node)

            neighbors = graph[node]
            #getting the neighbors of the current node

            #we loop through the neighbors in reverse order to maintain the correct order in DFS
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

             #showing the current state of stack and visited nodes       
            print(f"Stack that are visited: {stack}")
            print(f"visited nodes in the order: {order}")
            print("-----")

#when the stack is empty, we return the order of visited nodes
    return order


#Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs_trace(graph, 'A'))
