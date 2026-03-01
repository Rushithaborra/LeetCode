class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        result = [""] * n
        
        # Sort scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        for i in range(n):
            rank = sorted_scores.index(score[i]) + 1
            
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
        
        return result