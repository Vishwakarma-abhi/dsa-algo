class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        right[n-1] = 1
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]

        output = [0] * n
        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output