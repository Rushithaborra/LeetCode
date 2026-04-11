class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check box
                box = (i // 3, j // 3)
                if box not in boxes:
                    boxes[box] = set()

                if val in boxes[box]:
                    return False
                boxes[box].add(val)

        return True
