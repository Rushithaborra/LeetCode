class Solution(object):
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # left shift
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # right shift
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
        return True