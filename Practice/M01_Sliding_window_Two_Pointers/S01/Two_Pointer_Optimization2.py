'''
question 26 remove duplicates from sorted array

from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            
        
    return i+1
nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
'''
#Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Problem requires 1-based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # Return an empty list if no pair is found (problem constraints guarantee one solution).        
        return []