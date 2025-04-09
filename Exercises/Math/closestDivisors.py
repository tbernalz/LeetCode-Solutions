import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        """
        Finds the two closest integers (in absolute difference) whose product equals either `num + 1` or `num + 2`.

        Args:
            num (int): The given integer.

        Returns:
            List[int]: The closest two divisors.
        """

        def find_closest_divisors(n: int) -> List[int]:
            closest_divisors = (1, n)
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    if abs(closest_divisors[0] - closest_divisors[1]) > abs(i - n // i):
                        closest_divisors = (i, n // i)

            return closest_divisors

        divisors1 = find_closest_divisors(num + 1)
        divisors2 = find_closest_divisors(num + 2)

        if abs(divisors1[0] - divisors1[1]) <= abs(divisors2[0] - divisors2[1]):
            return divisors1
        else:
            return divisors2
