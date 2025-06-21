"""
🧩 Problem: 35. Search Insert Position
Given a sorted array nums and a target value, return the index if the target is found.
If not, return the index where it would be inserted to keep the array sorted.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        return low

"""EXPLANATION"""
"""
This is a classic binary search.
If the target is found at mid, return mid.
If target is greater, move right (low = mid + 1).
If target is smaller, move left (high = mid - 1).
If not found, the correct insert position is where low ends up.

🧠 Example:
Input: nums = [1, 3, 5, 6], target = 2
    Mid = 1 → nums[1] = 3 > 2 → move left → high = 0
    Mid = 0 → nums[0] = 1 < 2 → move right → low = 1
    Loop ends → return low = 1 → Insert 2 at index 1
"""