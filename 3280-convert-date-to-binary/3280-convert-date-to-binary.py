class Solution(object):
    def convertDateToBinary(self, date):
        y, m, d = date.split('-')
        
        y = bin(int(y))[2:]
        m = bin(int(m))[2:]
        d = bin(int(d))[2:]
        
        return y + "-" + m + "-" + d