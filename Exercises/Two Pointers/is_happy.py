class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Define if a number is happy based on some rules

        Args:
            n(int): The number to check

        Returns:
            bool: True if the number is happy, False otherwise
        """

        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
