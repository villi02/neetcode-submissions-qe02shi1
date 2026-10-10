class Solution:
    def climbStairs(self, n: int) -> int:
        """
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 3
            
            return climb(n-2) + climb(n-1)
        
        return climb(n)
        """
        if n <= 2:
            return n

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]