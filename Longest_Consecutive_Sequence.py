class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # pattern - Hashset + Sequence Start

        # Prepare a Hashset for fast lookup
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        # Define the Longest Length
        longest = 0

        for num in nums_set:

            if num - 1 not in nums_set:
                length = 1
                current = num

                # Extendthe sequence
                while current + 1 in nums_set:
                    current += 1
                    length += 1

                # Update the Answer (Longest Sequence found)
                longest = max(longest, length)

        return longest
