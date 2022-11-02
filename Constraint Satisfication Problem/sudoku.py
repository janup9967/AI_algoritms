N = 9
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()
# Checks whether it will be legal to assign num to the given row, col
def isSafe(grid, row, col, num):

	# Check if we find the same num in the similar row , we return false
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Check if we find the same num in the similar column , we return false
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Check if we find the same num in the particular 3*3 matrix, we return false
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True
# Takes a partially filled-in grid and attempts to assign values to all unassigned locations in such a way to meet the requirements for
def solveSudoku(grid, row, col):

	# Check if we have reached the 8th row and 9th column (0 indexed matrix) 
	if (row == N - 1 and col == N):
		return True
	
	if col == N:
		row += 1
		col = 0

	# Check if the current position of the grid already contains value >0, we iterate for next column
	if grid[row][col] > 0:
		return solveSudoku(grid, row, col + 1)
	for num in range(1, N + 1, 1):
	
		if isSafe(grid, row, col, num):
		
			grid[row][col] = num

			if solveSudoku(grid, row, col + 1):
				return True
 
		grid[row][col] = 0
	return False

 
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSudoku(grid, 0, 0)):
	printing(grid)
else:
	print("no solution exists ")


''' Output:-
3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7 
9 7 4 8 6 3 1 2 5 
8 5 1 7 9 2 6 4 3 
1 3 8 9 4 7 2 5 6 
6 9 2 3 5 1 8 7 4 
7 4 5 2 8 6 3 1 9 
