class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowCheck = {}
        columnCheck = {}
        squareCheck = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if r not in rowCheck:
                    rowCheck[r] = set()
                if c not in columnCheck:
                    columnCheck[c] = set()
                if (r//3,c//3) not in squareCheck:
                    squareCheck[(r//3,c//3)] = set()

                if  board[r][c] in rowCheck[r] or board[r][c] in columnCheck[c] or board[r][c] in squareCheck[(r // 3, c // 3)]:
                    return False
                rowCheck[r].add(board[r][c])
                columnCheck[c].add(board[r][c])
                squareCheck[(r // 3, c // 3)].add(board[r][c]) 
        return True