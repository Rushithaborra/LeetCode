class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        word = ['?'] * (n + m - 1)

        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                    else:
                        return ""

        # Helper to check F condition (ONLY when fully formed)
        def violates_F(pos):
            for i in range(max(0, pos - m + 1), min(n, pos + 1)):
                if str1[i] == 'F':
                    segment = word[i:i + m]
                    if '?' not in segment and "".join(segment) == str2:
                        return True
            return False

        # Step 2: Fill safely
        for i in range(len(word)):
            if word[i] == '?':
                for ch in ['a', 'b']:
                    word[i] = ch
                    if not violates_F(i):
                        break
                else:
                    return ""

        # Final safety check (VERY IMPORTANT)
        for i in range(n):
            if str1[i] == 'F':
                if "".join(word[i:i + m]) == str2:
                    return ""

        return "".join(word)