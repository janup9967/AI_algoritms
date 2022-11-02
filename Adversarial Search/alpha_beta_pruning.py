# define alpha and beta
alpha = float('-inf')
beta = float('inf')

def alpha_beta_pruning(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
  
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = alpha
 
        # Recur for left and right children
        for i in range(0, 2):
             
            val = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Alpha Beta Pruninga
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = beta
 
        # Recur for left and
        # right children
        for i in range(0, 2):
          
            val = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best


# main funcion 
score = [] # store values of leaf node
x = int(input("Enter total number of leaf node :- "))
for i in range(x):
  y = int(input("Enter the node value :- "))
  score.append(y)

d = int(input("Enter the depth value :- "))
node = int(input("Enter the nodes :-  "))

print("The optimal value is :", alpha_beta_pruning(d, node, True, score, alpha, beta))

''' Output:
    Enter total number of leaf node :- 8
Enter the node value :- 3
Enter the node value :- 5
Enter the node value :- 6
Enter the node value :- 9
Enter the node value :- 1
Enter the node value :- 2
Enter the node value :- 0
Enter the node value :- -1
Enter the depth value :- 0
Enter the nodes :-  0
The optimal value is : 5
'''
