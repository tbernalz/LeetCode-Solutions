class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Create an array of booleans based on divisibility by 5 of binary prefixes.

        Args:
            nums(list[int]): The binary array to analyze.

        Returns:
            list[bool]: An array of booleans where answer[i] is True if xi is divisible by 5.
        """
        answer = []
        current_number = 0

        for num in nums:
            current_number = (current_number * 2 + num) % 5
            answer.append(current_number == 0)

        return answer
