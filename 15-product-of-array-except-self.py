# Using extra space 
# Keep left and right multiplication valus in seperate arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # 1 <--------
        # -> 2 <-----
        # ---> 3 <---
        # --------> 4
        
        left = []
        right = []
        
        prev = 1
        for i in range(len(nums)):
            left.append(prev * nums[i])
            prev *= nums[i]
        
        prev = 1        
        for i in range(len(nums)):
            right.append(prev * nums[len(nums)-1-i])
            prev *= nums[len(nums)-1-i]
                
        ret = []
        for k in range(len(nums)):
            # left side
            if k == 0:
                ret.append(right[len(nums)-2])
                
            # right side
            elif k == len(nums) - 1:
                ret.append(left[len(nums)-2])
            
            # middle
            else:
                ret.append(left[k-1] * right[len(nums)-k-2])
                
        return ret
      

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 152 ms
# Memory Usage: 21 MB