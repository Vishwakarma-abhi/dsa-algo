class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        longest = 0
        max_freq = 0

        for right in range(len(s)):

            # Let's Build the frequency table for characters
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the maximum frequency
            max_freq = max(max_freq, freq[s[right]])

            # What if the window becomes invalid
            while (right-left+1) - max_freq > k:
                # Time for shrinking or replacement we do it from left
                freq[s[left]] -= 1
                left += 1

            # Update the answer
            longest = max(longest, right-left+1)

        return longest
