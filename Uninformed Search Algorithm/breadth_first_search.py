def bfs(graph, vertex, goal):  # function which takes graph source and goal as input
    visited = [vertex]  # to check a node is visited or not
    queue = [vertex]  # queue with source in it
    while queue:
        deVertex = queue.pop(0)  # poping the first element of queue
        if deVertex == goal:
            print(f'The goal is found :- {goal}')  # if goal is found then stop the code
            break
        print(deVertex)
        for adjacentVertex in graph[deVertex]:  # inserting neighbour of current node in queue
            if adjacentVertex not in visited:
                visited.append(adjacentVertex)
                queue.append(adjacentVertex)


graph = {"a": ["b", "c"],
         "b": ["a", "d", "e"],
         "c": ["a", "e"],
         "d": ["b", "e", "f"],
         "e": ["d", "f", "c"],
         "f": ["d", "e"]
         }

bfs(graph, 'a', 'f')

''' Output:-
a
b
c
d
e
The goal is found :- f
'''
