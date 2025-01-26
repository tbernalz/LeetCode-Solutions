class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Sort an array by parity. Move all the even integers at the beginning of the array followed by all the odd integers.

        Args:
            nums(list[int]): The array to sort.

        Returns:
            list[int]: The array sorted by parity.
        """
        even_index = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[even_index], nums[i] = nums[i], nums[even_index]
                even_index += 1

        return nums
