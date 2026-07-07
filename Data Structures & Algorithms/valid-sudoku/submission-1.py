class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Row Number: set()
        rowMap = {i:set() for i in range(9)}
        # Column Number: set()
        colMap = {i:set() for i in range(9)}
        # (row//3,col//3): set()
        squareMap = {(i,j):set() for i in range(3) for j in range(3)}
        
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                value = board[row][col]
                # Row Check
                if value == ".":
                    continue
                if value in rowMap[row] or value in colMap[col] or value in squareMap[(row//3,col//3)]:
                    return False
                rowMap[row].add(value)
                colMap[col].add(value)
                squareMap[(row//3,col//3)].add(value)
        return True
                    

