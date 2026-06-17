class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        # Sliding Window Template
        '''
        for right in range(len(s)):

            while Invalid:
                shrink- current char already present from set and move left 
            
            expand add current character

            update answer 
        '''

        left = 0
        right = 0
        seen = set()

        while right < len(s):

            while s[right] in seen:
                # Shrink / keep removing from left
                seen.remove(s[left])
                left = left + 1

            seen.add(s[right])

            answer = max(answer, right-left+1)
            right += 1
        return answer
