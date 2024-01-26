from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                dp[i] = True
            else:
                j = i - 1
                while j >= 0:
                    if dp[j] and nums[j] >= i - j:
                        dp[i] = True
                        break
                    j -= 1

        return dp[-1]                


s = Solution()
# print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))

