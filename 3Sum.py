class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Three Sum -> x + y + z = 0  -> y + z = -x 
        # We fix nums[i] and then find the two sum 
        
        # For Every element -> nums[i]
        nums.sort()
        n = len(nums)
        final_triplet = []
        for i in range(len(nums)):
            # Skip the duplicates
            if i > 0 and nums[i] == nums[i-1]:
                # if curr element is same as previously processed element then it will create duplicate triplet
                continue

            # Fix the nums[i] and define the target
            target = -nums[i]

            # Define the Left pointer
            left = i + 1

            # define the Right Pointer 
            right = len(nums) - 1 
            # Find the Rest Two Number of the triplet sum 
            while left < right:

                # Calculate the sum 
                target_sum = nums[left] + nums[right]

                if target_sum == target:
                    triplet = [nums[i],nums[left],nums[right]]
                    final_triplet.append(triplet)

                    # Move points inward
                    left +=1
                    right -=1

                    #Optimization : Skip the Dulpicates for the left pointer
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                    


                elif target_sum > target:
                    # move to left
                    right = right - 1
                else:
                    # move to right
                    left = left + 1
        
        return final_triplet