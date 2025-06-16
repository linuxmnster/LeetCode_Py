"""
🧩 Problem: 1. Two Sum
Given an array nums and a target value target, 
return the indices of the two numbers such that they add up to the target.
"""

"""
This is an O(long n^2) complixity code which directly does the brute force
thsi is nothing but the logic of the Bubble Sort, this is not an optimal solution
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

###########################################################################################

"""EXPLANATION"""
"""
We are scanning the list once using a dictionary to remember what number we need to
reach the target.
For each number:
    If the current number already exists in the dictionary d, it means we previously saw a 
    number that needs this one to make the target. ✅ So we return their indices.
    Otherwise, we calculate target - nums[i] and store that as a needed number in d 
    with its index.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i
