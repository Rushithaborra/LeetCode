class Solution(object):
    def bitwiseComplement(self, n):
        b = bin(n)[2:]        # convert to binary
        flipped = ""

        for bit in b:
            if bit == '0':
                flipped += '1'
            else:
                flipped += '0'

        return int(flipped, 2)   # convert back to decimal