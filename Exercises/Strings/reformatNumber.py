class Solution:
    def reformatNumber(self, number: str) -> str:
        """
        Reformat a phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into
        blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:
        - 2 digits: A single block of length 2.
        - 3 digits: A single block of length 3.
        - 4 digits: Two blocks of length 2 each.
        The blocks are then joined by dashes.

        Args:
            number (str): The input phone number string.

        Returns:
            str: The reformatted phone number with digits grouped by dashes.
        """
        clean_number = number.replace(" ", "").replace("-", "")
        formatted_number = []
        pointer = 0

        while pointer < len(clean_number) - 4:
            formatted_number.append(clean_number[pointer : pointer + 3])
            pointer += 3

        if len(clean_number[pointer:]) == 4:
            formatted_number.append(clean_number[pointer : pointer + 2])
            formatted_number.append(clean_number[pointer + 2 :])
        else:
            formatted_number.append(clean_number[pointer:])

        return "-".join(formatted_number)
