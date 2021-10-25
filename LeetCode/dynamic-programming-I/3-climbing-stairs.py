class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n+1):
            tmp = b
            b = a + b
            a = tmp
        return b


assert Solution().climbStairs(2) == 2
assert Solution().climbStairs(3) == 3
assert Solution().climbStairs(4) == 5
