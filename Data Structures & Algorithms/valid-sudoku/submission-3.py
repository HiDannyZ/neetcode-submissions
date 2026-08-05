class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # What does the input look like?
            # How are empty spaces represented?
        # Constraints:
        

        # {index: set()}
        validRow = defaultdict(set)
        validCol = defaultdict(set)
        # (row//3,col//3)
        validSquare = defaultdict(set)

        rows = len(board)
        cols = len(board[0])


        for row in range(rows):
            for col in range(cols):
                val = board[row][col]

                if val == ".":
                    continue

                if val in validRow[row]:
                    return False
                
                if val in validCol[col]:
                    return False
                
                if val in validSquare[row//3,col//3]:
                    return False
                
                validRow[row].add(val)
                validCol[col].add(val)
                validSquare[row//3,col//3].add(val)
        return True



        