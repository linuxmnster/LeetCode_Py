"""
🧩 Problem: 66. Plus One
You are given a list of digits representing a non-negative integer.
Add one to the number and return the resulting list of digits.
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0

            if i == 0:
                return [1] + digits

"""EXPLANATION"""
"""
Start from the last digit and move left.
If adding 1 doesn’t make it 10, just add 1 and return.
If it becomes 10, set that digit to 0 and continue to the next left digit (carry forward).
If all digits are 9 (e.g. [9,9,9]), then you end up with [0,0,0] and need to add a leading 1,
so return [1] + digits.

🧠 Example:
Input: digits = [9, 9]

i = 1: digits[1] + 1 = 10 → set to 0

i = 0: digits[0] + 1 = 10 → set to 0, at first digit → return [1, 0, 0]

"""

# Time Complexity: O(n)
# Space Complexity: O(1)

"""
OTHER SOLUTIONS
"""
def f(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
    return [1] + arr

# Time Complexity: O(n)
# Space Complexity (excluding output): O(1)
# Space Complexity (including output): O(n) (in worst case when all 9s)

def g(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
    return [1] + [0]*len(arr)

# Time Complexity: O(n)
# Space Complexity (excluding output): O(1)
# Space Complexity (including output): O(n) (due to new list creation [1] + [0]*len(arr))

"""
f(arr) is the best overall — it's correct, efficient, and minimal in both logic and memory.

🔁 Comparison Table:
Function	Correctness	 Time	    Space 	                    Output Allocation	Readability
f(arr)	    ✅ Yes	    O(n)	   O(1)	                       Only if needed	    ✅ Clean
g(arr)	    ✅ Yes	    O(n)	   O(1)	                       Always allocates	    Slightly redundant
plusOne()	✅ Yes	    O(n)	   O(1)	                       Only if needed	    ✅ Good
"""