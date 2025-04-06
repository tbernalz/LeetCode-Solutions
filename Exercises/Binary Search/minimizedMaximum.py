import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        Finds the minimum possible maximum number of products any store receives when distributing
        all products across `n` stores according to the specified rules.

        Rules:
        1. Each store can receive at most one product type but any amount of it.
        2. After distribution, each store has some number of products (possibly 0).
        3. The goal is to minimize the maximum number of products given to any single store.

        Args:
            n (int): The number of specialty retail stores.
            quantities (List[int]): An array where quantities[i] represents the number of products
                                    of the i-th product type.

        Returns:
            int: The smallest possible maximum number of products any store receives after optimal distribution.

        """
        left = 1
        right = max(quantities)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            stores_needed = sum(math.ceil(q / mid) for q in quantities)

            if stores_needed <= n:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
