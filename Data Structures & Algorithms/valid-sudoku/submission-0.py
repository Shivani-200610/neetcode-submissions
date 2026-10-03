from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check every Row
        for row in board:
            s = set()
            for i in row:
                if i in s:
                    return False 
                elif i != '.':
                    s.add(i)

        # 2. Check every Column (Fixed parentheses & added missing s.add)
        for column in range(9):
            s = set()
            for row in range(9):
                i = board[row][column]
                if i in s:
                    return False 
                elif i != '.':
                    s.add(i)

        # 3. Check every 3x3 Box (Fixed the row/col math formulas)
        for current in range(9):
            rowindex = 3 * (current // 3)
            colindex = 3 * (current % 3)
            s = set()
            for row in range(rowindex, rowindex + 3):
                for col in range(colindex, colindex + 3):
                    i = board[row][col]
                    if i in s:
                        return False 
                    elif i != '.':
                        s.add(i)
                        
        return True                
