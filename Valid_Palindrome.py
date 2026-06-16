class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Let's build normalized string

        normal_str = ""
        for ch in s.lower():
            isalphanum = ("a" <= ch <= "z") or (
                "A" <= ch <= "Z") or ("0" <= ch <= "9")

            if isalphanum:
                normal_str += ch

        left = 0
        right = len(normal_str) - 1

        while (left < right):

            if normal_str[left] != normal_str[right]:
                return False

            left += 1
            right -= 1

        return True
