class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        shop_list = {}
        for i in range(len(t)):
            shop_list[t[i]] = shop_list.get(t[i], 0)+1

        window = {}
        left, right = 0, 0

        # required - means number of unique required characters
        required = len(shop_list)

        # Formed - how many requirements are satisfied
        formed = 0

        # best answer
        best_left = 0
        best_length = float('inf')

        while right < len(s):
            ch = s[right]
            # Add new item to the shopping bag
            window[ch] = window.get(ch, 0)+1

            if ch in shop_list and window[ch] == shop_list[ch]:
                formed += 1  # this means one character found/formed

            while formed == required:
                # save the best answer
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_left = left

                # Shrink the window
                left_char = s[left]

                # Can we remove the leftmost item ?
                if left_char in shop_list and window[left_char] == shop_list[left_char]:
                    formed -= 1

                window[left_char] -= 1
                left += 1
            right += 1
        # No valid answer
        if best_length == float('inf'):
            return ""

        # Donot build the substring during traversal store the start and length
        return s[best_left:best_left + best_length]
