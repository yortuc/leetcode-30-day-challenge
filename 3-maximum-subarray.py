# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# =======================

# Applications:
# - In computer vision, maximum-subarray algorithms are used on bitmap images to detect the brightest area in an image.
# - Genomic sequence analysis employs maximum subarray algorithms to identify important biological segments of protein sequences.

# Kadane's Algorithm
# If dp[i] denotes the max sub array ending at index i
# dp[i] = max(dp[i-1], 0) + arr[i]    i: 0->n-1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = 0
        max_so_far = float('-inf')
        
        for n in nums:
            max_ending_here = max_ending_here + n
                
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
            if max_ending_here < 0:
                max_ending_here = 0
            
        return max_so_far