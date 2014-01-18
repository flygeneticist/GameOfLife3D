# Title: Game of life in 2D
# Written by: Kevin Keller
# Created on: 01/18/2014

# Game will be played out on a 2D grid of 10 x 10 spaces
# The first generation is created by applying the above rules simultaneously to every cell in the seed.
# The rules continue to be applied repeatedly to create further generations.

# Rules:
# 1) Any live cell with fewer than two live neighbours dies, as if by needs caused by underpopulation.
# 2) Any live cell with more than three live neighbours dies, as if by overcrowding.
# 3) Any live cell with two or three live neighbours lives, unchanged, to the next generation.
# 4) Any dead cell with exactly three live neighbours becomes a live cell.

import numpy as np

# setup the grid as a generated numpy array
grid = np.random.randint(0,2,(10,10))

def count_neighbors(grid):
    # Count neighbours for cells
    N = (grid[0:-2,0:-2] + grid[0:-2,1:-1] + grid[0:-2,2:] +
         grid[1:-1,0:-2]                + grid[1:-1,2:] +
         grid[2:  ,0:-2] + grid[2:  ,1:-1] + grid[2:  ,2:])

    # Apply the rules
    birth = (N==3) & (grid[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (grid[1:-1,1:-1]==1)
    grid[...] = 0
    grid[1:-1,1:-1][birth | survive] = 1
    return grid

print("Starting grid:")
print(grid)

for i in range(10): 
	count_neighbors(grid)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(grid)
