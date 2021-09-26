class Solution:
    moves = 0
    def movesToChessboard(self, board: List[List[int]]) -> int:
      n = len(board)
      for i in range(0,n):
        traverseRow(board[i])
        traverseCol(board, i)

      return Solution.moves if Solution.moves != 0 else -1   ## solution.moves or just moves ???


    def traverseCol(self, board, i):
      pass

    def traverseRow(self, row):
      pass

    def switchCols(self, board):
      pass

    def switchRows(self, board):
      pass
