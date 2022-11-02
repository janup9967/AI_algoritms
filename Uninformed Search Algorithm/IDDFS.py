graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

path = list()

def DFS(inital,goal,graph,maxDepth,curList):
    print("Checking for goal",inital)
    curList.append(inital)
    if inital==goal:
        print("\nGoal Node successfully found ")
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[inital]:
        if DFS(node,goal,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDFS(inital,goal,graph,maxDepth):
    for i in range(maxDepth):
        print("\nCurrent Level :- ",i)
        curList = list()
        if DFS(inital,goal,graph,i,curList):
            return True
    return False

inital = 'A'
goal = input("Enter the goal node :- ")
maxDepth = int(input("Enter the maximum depth limited :- "))


if not iterativeDFS(inital,goal,graph,maxDepth):
    print("\nNo path available for the goal node in the given depth")
else:
    print("\nPath to goal node available in the given depth ")
    print(path.pop())
    
    
    
'''Output:- 
Enter the goal node :- E
Enter the maximum depth limited :- 4

Current Level :-  0
Checking for goal A

Current Level :-  1
Checking for goal A
Checking for goal B
Checking for goal C

Current Level :-  2
Checking for goal A
Checking for goal B
Checking for goal D
Checking for goal E

Goal Node successfully found 

Path to goal node available in the given depth 
['A', 'B', 'E']
'''
