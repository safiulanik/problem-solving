from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            current = cost[i] + min(first, second)
            first = second
            second = current
        return min(first, second)


assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
assert Solution().minCostClimbingStairs(
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
