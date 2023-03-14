# Create a variable with the original grid
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

# Create a function to change the dashes in the grid to numbers
def minesweeper(grid):
    # Create a variable with the number of rows in the grid and create a list of directions
    rows = len(grid)
    if(rows == 0):
        return
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    # Create a variable with the number of columns in the grid
    columns = len(grid[0])
    # Create the new grid using for loops and if statements
    newgrid = [["#" for j in range(columns)] for i in range(rows)]
    for row in range(rows):
        for column in range(columns):
            if(grid[row][column] == "-"):
                count = 0
                # Create a for loop using the directions list to create new rows and columns
                for direction in directions:
                    newrow = row + direction[0]
                    newcolumn = column + direction[1]
                    if(newrow >= 0 and newrow < rows and newcolumn >=0 and newcolumn < columns and grid[newrow][newcolumn] == "#"):
                        count = count + 1
                newgrid[row][column] = count
    return newgrid
# Print the new grid
newgrid = minesweeper(grid)
print(newgrid)