class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup_map = {}
        for i in range(len(nums)):
            lookup_map[nums[i]] = i
        ans = []
        for i in range(len(nums)):
            rem_target = target - nums[i]

            if rem_target in lookup_map and i != lookup_map[rem_target]:
                ans = [i, lookup_map[rem_target]]
                break

        return ans
