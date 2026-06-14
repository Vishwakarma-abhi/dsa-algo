class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach - 1 - brute force 
        '''
        Pick One Element Once Search for his Duplicate if found return false else 
        no found then return true
        '''

        # Approach 2 - Optimal - Using Maps
        unique_set = set()
        for i in range(len(nums)):
            unique_set.add(nums[i])
        
        has_duplicates = not (len(nums) == len(unique_set))

        return has_duplicates