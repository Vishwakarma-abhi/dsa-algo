class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers)-1

        while left < right:

            # calculate sum
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                ans = [left+1, right+1]
                break

            if curr_sum > target:
                # move to left
                right = right - 1
            if curr_sum < target:
                # move to right
                left = left + 1

        return ans
