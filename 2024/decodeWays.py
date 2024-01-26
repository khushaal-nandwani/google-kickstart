class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]

        # because we need previous two elements, we create two base cases

        for i in range(len(s)):
            print(dp, s[i], s)
            # base case 1
            if i == 0:
                dp[i] = 1
            # base case 2
            if i == 1:
                # if the combined elements can be interpreted as 26 or below
                if 0 < int(s[i - 1]) < 3 and int(s[i]) < 7:
                    # then possible ways are 2
                    dp[i] = 2
                else:
                    dp[i] = 1

            # the element by itself can always be interpreted as 1
            # so ways are at least as much the previous one had
            total = dp[i - 1]

            # if the previous and this element together can be interpreted as 26 or below
            if 0 < int(s[i - 1]) < 3 and int(s[i]) < 7:
                # all the ways is i - 2 must also be added
                total += dp[i - 2]

        print(dp, s[i], s)

        return dp[-1]


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
