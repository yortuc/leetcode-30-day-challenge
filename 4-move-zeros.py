# Non in-pace
# Using additional space
# O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        non_zeros = []
        
        for n in nums:
            if n != 0:
                non_zeros.append(n)
                
        for i in range(len(nums)):
            if i < len(non_zeros):
                nums[i] = non_zeros[i]
            else:
                nums[i] = 0

# ---------------------------
# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 15 MB
# ---------------------------

# In-place solution?

