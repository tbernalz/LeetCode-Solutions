from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Shuffle the array using the Fisher-Yates algorithm.

        Returns:
            List[int]: A randomly shuffled array.
        """
        nums_shuffled = self.nums.copy()

        for i in range(len(nums_shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            nums_shuffled[i], nums_shuffled[j] = nums_shuffled[j], nums_shuffled[i]

        return nums_shuffled
