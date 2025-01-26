class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        """
        Calculate the minimum number of operations required to make the strings equal.
        In one operation, you can choose one of these strings and delete its rightmost character.

        Args:
            s1(str): The first string to analyze.
            s2(str): The second string to analyze.
            s3(str): The third string to analyze.

        Returns:
            int: The minimum number of operations required to make the strings equal, or -1 if impossible.
        """

        min_length = min(len(s1), len(s2), len(s3))
        common_prefix_length = 0

        for i in range(min_length):
            if s1[i] == s2[i] == s3[i]:
                common_prefix_length += 1
            else:
                break

        if common_prefix_length == 0:
            return -1

        s1_operations = len(s1) - common_prefix_length
        s2_operations = len(s2) - common_prefix_length
        s3_operations = len(s3) - common_prefix_length

        return s1_operations + s2_operations + s3_operations
