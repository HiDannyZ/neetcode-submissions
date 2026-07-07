class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        firstLetter = word[0]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == firstLetter:
                    if self.search(board, word,row,col,0):
                        return True
        return False

    def search(self, board, word,row,col, index):
        if index == len(word):
            return True
        if row < 0:
            return False
        if col < 0: 
            return False
        if row >= len(board):
            return False
        if col >= len(board[0]):
            return False
        if board[row][col] != word[index]:
            return False
        savedValue = board[row][col]
        board[row][col] = "#"
        res = self.search(board,word,row + 1,col,index+1) or self.search(board,word,row-1,col,index+ 1) or self.search(board,word,row,col+1,index+1) or self.search(board,word,row,col-1,index+1)
        board[row][col] = savedValue
        return res
