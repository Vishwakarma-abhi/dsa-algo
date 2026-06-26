class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # Left partition should contain half the elements
        total_left = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:

            # Number of elements taken from nums1
            cut1 = (low + high) // 2

            # Remaining elements come from nums2
            cut2 = total_left - cut1

            # Boundary elements around the partition

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]

            # FIX: Should be +inf, not -inf
            right1 = float('inf') if cut1 == m else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

            # FIX: Should be +inf, not -inf
            right2 = float('inf') if cut2 == n else nums2[cut2]

            # Correct partition found
            if left1 <= right2 and left2 <= right1:

                # Odd total elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total elements
                return (max(left1, left2) + min(right1, right2)) / 2

            # Too many elements taken from nums1
            elif left1 > right2:
                high = cut1 - 1

            # Too few elements taken from nums1
            else:
                low = cut1 + 1