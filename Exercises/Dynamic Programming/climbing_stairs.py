class Solution:
    def __init__(self):
        self.climb_stairs_cache = {}

    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of ways to climb to the top of a staircase, given that each step can be either 1 or 2 steps.

        Args:
            n(int): Number of stairs to be climbed.

        Returns:
            int: The number of ways to climb to the top.
        """

        if n in self.climb_stairs_cache:
            return self.climb_stairs_cache[n]

        elif n == 0:
            return 0

        elif n == 1:
            return 1

        elif n == 2:
            return 2

        else:
            value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.climb_stairs_cache[n] = value
            return value
