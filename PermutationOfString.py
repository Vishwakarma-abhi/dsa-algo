class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Calculate the frequency map of the String S1
        s1_freq = {}
        
        for ch in range(len(s1)):
            s1_freq[s1[ch]]= s1_freq.get(s1[ch],0) + 1

        
        # Now calculate the window size - Fixed
        window_size = len(s1)
        wind_freq = {}

        # let's build first window freq
        for i in range(window_size):
            wind_freq[s2[i]] =  wind_freq.get(s2[i],0) + 1
        
        if s1_freq == wind_freq:
            return True

        left = 0
        right = window_size
        while right < len(s2):
            wind_freq[s2[left]] -= 1

            if wind_freq[s2[left]] == 0:
                # delete it 
                del wind_freq[s2[left]]
            

            wind_freq[s2[right]] = wind_freq.get(s2[right],0) + 1

            if s1_freq ==  wind_freq:
                return True
            left +=1
            right +=1

        return False

