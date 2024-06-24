#Program for manipulating 2-dimensional arrays of size.
#Ntobeko Mhlongo
#19 April 2024


def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):#Iterating over each row index from 0 to 3
        grid.append([0] * 4) # Creating a 4x4 grid

def print_grid(grid):
    """Print out a 4x4 grid in 5-width columns within a box."""
    print("+" + "-" * 20 + "+") # Printing the top border of the grid box
    for row in grid:
        print("|", end="") # Printing the left border of the grid box
        for num in row:
            if num != 0:
                num_width = len(str(num)) # Determining the width of the current number (1 or 2 digits)
                padding = " " * (5 - num_width) # Calculating the padding required to make each column 5-width
                print(num, end=padding) # Printing the number with the appropriate padding
            else:
                print("     ", end="") # Printing spaces instead of 0s
        print("|") # Printing the right border of the grid box
    print("+" + "-" * 20 + "+") # Printing the bottom border of the grid box


def check_lost(grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""     
    for i in range(4):
        for j in range(4): # Checking if the current cell contains 0 and if there are adjacent cells with the same value
            if grid[i][j] == 0:
                return False
            if i > 0 and grid[i][j] == grid[i-1][j]:
                return False
            if i < 3 and grid[i][j] == grid[i+1][j]:
                return False
            if j > 0 and grid[i][j] == grid[i][j-1]:
                return False
            if j < 3 and grid[i][j] == grid[i][j+1]:
                return False
    return True # Returning true if none of the above conditions were met

def check_won(grid):
    """Return True if a value >= 32 is found in the grid; otherwise False."""
    for row in grid:
        for num in row:
            if num >= 32:
                return True # Returning true if any cell is greater or equal to 32
    return False # Otherwise false

def copy_grid(grid):
    """Return a copy of the given grid."""
    new_grid = [] # Starting an empty grid to store the copied values
    for row in grid:
        copied_row = [] # Creating a new list containing the same elements as the current row
        for element in row:
            copied_row.append(element) # Appending each element to the copied row
        new_grid.append(copied_row) # Appending the copied row to the new grid
    return new_grid


def grid_equal(grid1, grid2):
    """Check if 2 grids are equal - return boolean value."""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]: # Returning false if the 2 grids are not equal
                return False
    return True