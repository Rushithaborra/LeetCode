class Solution(object):
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)

        # Frequency array
        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0

        for price in range(1, max_cost + 1):
            if freq[price] > 0:
                can_buy = min(freq[price], coins // price)
                count += can_buy
                coins -= can_buy * price

                if coins < price:
                    break

        return count