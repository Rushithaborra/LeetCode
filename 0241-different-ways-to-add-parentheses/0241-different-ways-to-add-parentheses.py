class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def solve(exp):
            if exp in memo:
                return memo[exp]

            result = []

            for i in range(len(exp)):
                char = exp[i]
                if char in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i+1:])
                    for l in left:
                        for r in right:
                            if char == "+":
                                result.append(l + r)
                            elif char == "-":
                                result.append(l - r)
                            else:
                                result.append(l * r)

            if not result:
                result.append(int(exp))

            memo[exp] = result
            return result

        return solve(expression)