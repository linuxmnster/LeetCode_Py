"""
🧩 Problem: 27. Remove Element
Given an array nums and a value val, remove all occurrences of val in-place and 
return the new length.
You can change the order of elements, but you must not use extra space.
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

"""EXPLANATION"""
"""
k keeps track of the position where we place elements not equal to val.
For each element in nums:
If it’s not equal to val, copy it to position k and increment k.
This way, all valid (non-val) elements are packed at the start of the array.

🧠 Example:
Input: nums = [3,2,2,3], val = 3

nums[0] = 3 → skip

nums[1] = 2 → place at nums[0] → nums = [2,2,2,3]

nums[2] = 2 → place at nums[1] → nums = [2,2,2,3]

nums[3] = 3 → skip

Final array: [2, 2, ...], Return k = 2
"""

