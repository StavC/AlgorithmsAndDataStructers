class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                elif c in rows[i] or c in cols[j] or c in box[(i // 3) * 3 + j // 3]:
                    return False

                rows[i].add(c)
                cols[j].add(c)
                box[(i // 3) * 3 + j // 3].add(c)

        return True
