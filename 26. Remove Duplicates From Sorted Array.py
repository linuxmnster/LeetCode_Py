"""
🧩 Problem: 26. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in-place such that each element appears only once and 
return the new length.
Do not use extra space. Modify the original array in-place.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i

"""EXPLANATION"""
"""
i tracks the position to insert the next unique number.
j scans through the array.
Since the array is sorted, duplicates will be next to each other.
If nums[j] != nums[j-1], it means nums[j] is a new unique number:
Place it at position i.
Move i forward.
Finally, return i, the count of unique elements.
"""

#TIME COMPLEXITY : O(Log n)
#SPACE COMPLEXITY : O(1)