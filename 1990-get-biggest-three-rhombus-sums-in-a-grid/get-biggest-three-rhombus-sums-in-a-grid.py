class Solution(object):
    def getBiggestThree(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        sums = set()

        for r in range(rows):
            for c in range(cols):

                # size 0 rhombus (single cell)
                sums.add(grid[r][c])

                size = 1
                while True:
                    if r-size < 0 or r+size >= rows or c-size < 0 or c+size >= cols:
                        break

                    total = 0

                    # top -> right
                    i, j = r-size, c
                    for k in range(size):
                        total += grid[i+k][j+k]

                    # right -> bottom
                    i, j = r, c+size
                    for k in range(size):
                        total += grid[i+k][j-k]

                    # bottom -> left
                    i, j = r+size, c
                    for k in range(size):
                        total += grid[i-k][j-k]

                    # left -> top
                    i, j = r, c-size
                    for k in range(size):
                        total += grid[i-k][j+k]

                    sums.add(total)

                    size += 1

        return sorted(sums, reverse=True)[:3]