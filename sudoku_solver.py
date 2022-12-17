# Drawing the Sudoku board to be solved. 0's represent empty spaces in the puzzle to be filled by the player
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Function to print the Sudoku board before solving
def print_board(board):
    i = 0
    while (i < len(board)):
        if ((i%3 == 0) and (i != 0)):       # Printing a horizontal division line every three rows (accounting for the sub-matrices)
            print("- - - - - - - - - - - - - ")
        j = 0
        while (j < len(board[i])):
            if ((j%3 == 0) and (j != 0)):       # Printing a vertical division line every three columns (accounting for the sub-matrices0)
                print(" |  ", end = "")
            
            curr = board[i][j]
            if (j == 8):        # Print such that the elements of the succeeding row appears on the next line
                if (curr == 0):
                    print("_")
                else:
                    print(str(curr))     
            else:       # Print such that the elements of the same row appear on the same line
                if (curr == 0):
                    print("_ ", end = "")
                else:
                    print(str(curr) + " ", end = "")
            j += 1
        i += 1


# Function to find the first empty cell in the board
def find_empty(board):
    i = 0
    while (i < len(board)):     # iterating through the board till an empty cell is found
        j = 0
        while (j < len(board[i])):
            if (board[i][j] == 0):      # Empty cell found, return the position of the cell
                return (i, j)
            j += 1
        i += 1
    return (None, None)     # All cells are filld, return None


# Function to test the validity of the Sudoku board (if it fits the rules of the Sudoku puzzle)
def is_valid(board, cell_test, cell_pos):
    row, col = cell_pos
    
    # Rows
    i = 0
    while (i < len(board[row])):
        if (cell_test == board[row][i]):
            return False
        i += 1

    # Columns
    j = 0
    while (j < len(board)):
        if (cell_test == board[j][col]):
            return False
        j += 1

    # Check box
    box_x = cell_pos[1] // 3
    box_y = cell_pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == cell_test and (i,j) != cell_pos:
                return False
    
    return True

# Solving the Sudoku board by Backtracking
def solve_sudoku(board):
    (row, col) = find_empty(board)
    if ((not row) and (not col)):      # no empty cells remaining in the board
        return True
    
    num = 1     # the example number to be tested
    while (num < 10):
        test_valid = is_valid(board, num, (row, col))
        if (test_valid):
            board[row][col] = num
            if (solve_sudoku(board)):
                return True
        board[row][col] = 0
        num += 1
    
    return False

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Sudoku Puzzle: \n")
    print_board(board)
    print("\n")
    print("Solved Sudoku board:\n")
    solved = board
    solve_sudoku(solved)
    print_board(solved)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

if __name__ == "__main__":
    main()