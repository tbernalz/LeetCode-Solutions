class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        """
        Calculate the account balance after rounding the purchase amount and deducting from $100.

        The purchase amount is rounded to the nearest multiple of 10:
        - If the remainder when divided by 10 is less than 5, round down.
        - Otherwise, round up.

        Args:
            purchaseAmount (int): The purchase amount.

        Returns:
            int: The remaining account balance after deducting the rounded purchase amount.
        """
        remainder = purchaseAmount % 10

        if remainder < 5:
            roundedAmount = purchaseAmount - remainder
        else:
            roundedAmount = purchaseAmount + (10 - remainder)

        return 100 - roundedAmount
