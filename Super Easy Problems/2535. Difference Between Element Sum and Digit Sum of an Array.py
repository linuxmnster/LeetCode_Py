"""
🧩 Problem: 2535. Difference Between Element Sum and Digit Sum of an Array

Given an integer array nums, you must calculate:
Element Sum → sum of all elements in the array
Digit Sum → sum of digits of each element
Return the absolute difference between the two sums.
You solved this using a single running variable and performing additions/subtractions on the same accumulator.
"""

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a += i
            if a < 10:
                a -= i
            else:
                while i:
                    a -= (i % 10)
                    i //= 10
        return abs(a)

"""🧠 EXPLANATION
You use one variable a to dynamically track the difference:

Step-by-step idea:
Add the number i to a.
If the running value is still below 10, you remove the same number back — meaning its digits will be handled naturally later.
Otherwise, you subtract each digit of the number:
Extract each digit using i % 10
Subtract it from a
Reduce the number using integer division

Effectively:
a = a + element_sum  - digit_sum
But done in one combined process.
Finally, you return:
abs(a)
which is the required difference.

📘 Example
Input:
nums = [1, 15, 6, 3]
Processing:
Add 1 → below 10 → subtract
Add 15 → now >= 10 → subtract its digits (1 + 5)
Add 6 → subtract 6
Add 3 → subtract 3
Final result → abs(25 - 16) = 9

Output:
9

⏱️ TIME COMPLEXITY: O(n · k)
n → number of elements
k → number of digits per element
Still extremely efficient.

🧠 SPACE COMPLEXITY: O(1)
Only a single integer variable is used."""