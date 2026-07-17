class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # choice 1 ->  pick it
            subset.append(nums[i])
            # explore
            dfs(i+1)
            # choice 2 -> exclude it
            subset.pop()
            # explore without it
            dfs(i+1

        
        dfs(0)
        return res

