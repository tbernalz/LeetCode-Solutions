class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        """
        Operate on an array to create a new one based on specific operations.

        Args:
            nums(list[int]): The array of numbers to process.

        Returns:
            list[int]: An array where each -1 is replaced by the last visited positive integer
            or -1 if no valid integer is available.
        """
        seen = []
        ans = []
        k = 0

        for num in nums:
            if num >= 0:
                seen.insert(0, num)
                k = 0
            else:
                if k < len(seen):
                    ans.append(seen[k])
                else:
                    ans.append(-1)
                k += 1

        return ans
