class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # Left is the position of the pivot
        # now we can decide which part to go for target
        pivot = left
        l, r = 0, len(nums) - 1

        # decide which half to conider for search

        if target >= nums[pivot] and target <= nums[r]:
            # this case means right part will be search space
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
