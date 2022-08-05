graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'G':['N','O'],
    'F':['L','M'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[]
    
}


def DLS(start, goal,path,level,maxDepth):
    print("\nCurrent Level :- ",level)
    print("Testing for Goal Node :- ",start)
    path.append(start)
    if start == goal:
        print("\nGoal Node successfully found ")
        return path
    if level == maxDepth:
        return False
    print("Expanding the Current Node :- ",start)
    for i in graph[start]:
        if DLS(i,goal,path,level+1,maxDepth):
            return path
        path.pop()
    return False
    


start = 'A'
goal = input("Enter the goal node :- ")
maxDepth = int(input("Enter the maximum depth limited :- "))
path = list()
dls = DLS(start,goal,path,0,maxDepth)
if (dls):
    print("\nPath to goal node available")
    print("\nPath :- ",path)
else:
    print("\nNo path available for the goal node in the given depth")