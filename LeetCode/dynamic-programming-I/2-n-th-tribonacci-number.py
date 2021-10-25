class Solution:
    def tribonacci(self, n: int, dp=None) -> int:
        if dp is None:
            dp = {
                0: 0,
                1: 1,
                2: 1
            }
        if n in dp.keys():
            return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]


assert Solution().tribonacci(4) == 4
assert Solution().tribonacci(25) == 1389537
assert Solution().tribonacci(37) == 2082876103
