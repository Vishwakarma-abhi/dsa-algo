class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:

            # Calculate the width
            width = right - left

            # Calcuate the height
            cont_height = min(heights[left], heights[right])

            # Calculate the Area
            area = width * cont_height

            # we update the max area
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                # move left
                left += 1
            else:
                right -= 1

        return max_area
