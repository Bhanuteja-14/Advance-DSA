from typing import List

'''
209. Minimum Size Subarray Sum

from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_len = float("inf")
    left = 0
    cur_sum = 0

    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))  # expected output: 2

'''
#713. Subarray Product Less Than K
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:  
        return 0
    
    count = 0
    prod = 1  
    left = 0  
    
    for right, num in enumerate(nums):
        prod *= num  
        while prod >= k:  
            prod /= nums[left]
            left += 1
        count += right - left + 1  
    
    return count
nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))  # expected output: 8