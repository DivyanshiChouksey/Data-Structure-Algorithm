# Valid Sudoku

"""
    as per conditions:-
    1. check if each row of the borad stores only unique values from the range[1,9]
    2. check if each column of the borad stores only unique values from the range[1,9]
    3. check if all possible 3*3 submatrix of the borad stores only unique values from the range[1,9]
        for finding the starting coordinates of all 3*3 submatrix can dedue formula- firstly divide the coordinates
        by 3 then multiply it by 3 [ie. (i//3)*3 , (j//3)*3].
    
"""


# Time Complexity = O(1) || Space Complexity = O(1)

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def isValidSudoku(board):
    def check(i, j):
        digit = board[i][j]
        for m in range(len(board[0])):
            if j == m:
                continue
            if digit == board[i][m]:
                return False
        for n in range(len(board)):
            if i == n:
                continue
            if digit == board[n][j]:
                return False
        x = (i // 3) * 3
        y = (j // 3) * 3
        for m in range(x, x + 3):
            for n in range(y, y + 3):
                if i == m and j == n:
                    continue
                if board[i][j] == board[m][n]:
                    return False
                # print(board[m][n])

        return True

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            else:
                if check(i, j):
                    continue
                else:
                    return False

    return True


print(isValidSudoku(board))
