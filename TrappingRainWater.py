class Solution:
    def trap(self, height: List[int]) -> int:
        # let's build left and right max array for walls for each i
        n = len(height)

        if n == 0:
            return 0

        left_max = [0]*n
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        right_max = [0]*n
        right_max[n-1] = height[n-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # Now Let's Calculate the max water that can be Trapped
        water = 0
        for i in range(len(height)):

            water += min(left_max[i], right_max[i]) - height[i]

        return water
