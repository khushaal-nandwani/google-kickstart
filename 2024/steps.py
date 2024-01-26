import math
from typing import List

class Solution:
    def __init__(self):
        self.dp = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.dp = [-1] * n
        return min(self.OPT(cost, n-1), self.OPT(cost, n-2))

    def OPT(self, cost: List[int], index: int) -> int:
        """Returns the optimal cost"""
        if index < 0:
            return 0
        if index == 0:
            return cost[0]
        if index == 1:
            return cost[1]
        if self.dp[index] != -1:
            return self.dp[index]
        self.dp[index] = min(self.OPT(cost, index-1), self.OPT(cost, index-2)) + cost[index]
        return self.dp[index]

if __name__ == '__main__':
    # cost = [0, 2, 2, 1]
    cost = [1,100,1,1,1,100,1,1,100,1]
    # cost = [1,100,1,1,1,100,1,1,100,1]
    s = Solution()
    print(s.minCostClimbingStairs(cost))