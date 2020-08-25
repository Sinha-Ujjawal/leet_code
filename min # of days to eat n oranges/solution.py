from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def dp(m):
            if m < 3:
                return m
            return 1 + min(
                (m & 1) + dp(m >> 1),
                (m % 3) + dp(m // 3),
            )
        
        return dp(n)
