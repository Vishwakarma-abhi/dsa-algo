class Solution:

    def make_freq_map(self, my_string: str, my_map: dict):
        for ch in my_string:
            if ch in my_map:
                my_map[ch] += 1
            else:
                my_map[ch] = 1

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Step 1 Create maps for both
        s_map = {}
        t_map = {}

        self.make_freq_map(s, s_map)
        self.make_freq_map(t, t_map)

        for ch in s:
            if ch not in t_map:
                return False
            if s_map[ch] != t_map[ch]:
                return False
        return True
