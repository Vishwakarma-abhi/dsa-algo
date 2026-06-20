from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        # 1. Analyze and construct the dq for window 1
        for i in range(0, k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # 2. Initialize ans with the maximum of the first window
        ans = [nums[dq[0]]]

        # 3. Find max for all remaining windows
        for i in range(k, len(nums)):
            # Remove the element if it falls out of the sliding window
            # (Using 'if' is sufficient since only one element drops off per step)
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain the decreasing monotonic order
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

            # Append the maximum of the CURRENT window
            ans.append(nums[dq[0]])

        return ans
