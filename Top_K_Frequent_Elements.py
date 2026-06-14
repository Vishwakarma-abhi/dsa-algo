from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create the freq_map
        freq_map = defaultdict(int)
        for i in range(len(nums)):
            freq_map[nums[i]] += 1

        # Create  bucket array
        bucket = [[] for _ in range(len(nums)+1)]

        # Fill the buckets
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Traverse and find the highest

        ans = []
        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        return ans
