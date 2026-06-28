# revisit required 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        maxProd = nums[0]
        minProd = nums[0]

        for i in range(1,len(nums)):

            # Incase of Current < 0 - a negative number
            if nums[i] < 0:
                # we swap because negative * negative number produces the positive higher result 
                maxProd , minProd = minProd, maxProd
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i],minProd * nums[i])

            res = max(res,maxProd)
        
        return res