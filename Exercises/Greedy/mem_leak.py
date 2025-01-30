class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        """
        Simulates memory allocation to two memory sticks until a crash occurs.

        At each second i (starting from 1), i bits of memory are allocated to the memory stick
        with more available memory. If both sticks have the same available memory, allocation
        happens from the first stick. If neither stick has at least i bits available, the
        program crashes.

        Args:
            memory1 (int): The initial available memory on the first memory stick.
            memory2 (int): The initial available memory on the second memory stick.

        Returns:
            list[int]: A list containing [crashTime, memory1crash, memory2crash], where:
                - crashTime (int): The time when the program crashed.
                - memory1crash (int): The remaining memory in the first stick at crash time.
                - memory2crash (int): The remaining memory in the second stick at crash time.
        """
        time = 1

        while True:
            if memory1 >= memory2:
                if memory1 < time:
                    break
                memory1 -= time
            else:
                if memory2 < time:
                    break
                memory2 -= time
            time += 1

        return [time, memory1, memory2]
