from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Find all uncommon words between two sentences.
        A word is uncommon if it appears exactly once across both sentences.

        Args:
            s1 (str): First sentence of space-separated lowercase words.
            s2 (str): Second sentence of space-separated lowercase words.

        Returns:
            List[str]: List of uncommon words in any order.
        """
        word_counts = defaultdict(int)
        init = 0
        s3 = s1 + " " + s2

        for i in range(len(s3) + 1):
            if i == len(s3) or s3[i] == " ":
                word = s3[init:i]
                word_counts[word] = word_counts.get(word, 0) + 1
                init = i + 1

        return [word for word, count in word_counts.items() if count == 1]
