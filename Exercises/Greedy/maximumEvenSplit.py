from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        """
        Splits an integer into a sum of the maximum possible number of unique positive even integers.
        If no valid split exists for `finalSum`, an empty list is returned.

        Args:
            finalSum (int): The integer to be split.

        Returns:
            List[int]: A list of unique positive even integers that sum up to `finalSum`,
                       containing the maximum possible number of integers.
                       The integers can be returned in any order.
        """
        if finalSum % 2 != 0:
            return []

        result = []
        current_sum = 0
        next_num = 0

        while True:
            next_num += 2
            result.append(next_num)
            current_sum += next_num

            if current_sum == finalSum:
                return result

            elif current_sum > finalSum:
                overshoot_num = result.pop()
                current_sum -= overshoot_num
                remainder = finalSum - current_sum
                result[-1] += remainder
                return result
