from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        Identifies the two duplicated numbers in a list containing integers from 0 to n-1.

        Args:
            nums (List[int]): A list of integers containing exactly two duplicates.

        Returns:
            List[int]: A list containing the two duplicated numbers, in any order.
        """
        seen = set()
        duplicated = []

        for num in nums:
            if num in seen:
                duplicated.append(num)
                if len(duplicated) == 2:
                    break
            else:
                seen.add(num)

        return duplicated
