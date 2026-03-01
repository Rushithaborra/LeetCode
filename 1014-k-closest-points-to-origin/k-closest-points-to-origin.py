import random

class Solution(object):
    def kClosest(self, points, k):

        def distance(point):
            return point[0]*point[0] + point[1]*point[1]

        def quickselect(left, right):
            pivot_index = random.randint(left, right)
            pivot_distance = distance(points[pivot_index])

            # Move pivot to end
            points[pivot_index], points[right] = points[right], points[pivot_index]

            store_index = left

            for i in range(left, right):
                if distance(points[i]) <= pivot_distance:
                    points[i], points[store_index] = points[store_index], points[i]
                    store_index += 1

            # Move pivot to correct place
            points[store_index], points[right] = points[right], points[store_index]

            return store_index

        left, right = 0, len(points) - 1

        while left <= right:
            pivot_index = quickselect(left, right)

            if pivot_index == k:
                break
            elif pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        return points[:k]