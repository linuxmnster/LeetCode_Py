"""🧩 Problem: 2535. Difference Between Element Sum and Digit Sum of an Array
You are given an integer array nums.
Element Sum = sum of all numbers in the array
Digit Sum = sum of the digits of all numbers in the array
Return the absolute difference between the element sum and the digit sum."""

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a += i
            while i:
                a -= (i % 10)
                i //= 10
        return abs(a)

"""🧠 EXPLANATION
This solution cleverly computes the final answer using one variable (a) by combining addition and subtraction operations.

How It Works:
Add the whole number to a
This accumulates the element sum.

Subtract each digit of that number
Using a loop:

i % 10 extracts the last digit
a -= digit subtracts it
i //= 10 removes the last digit

After processing each number, a contains:
a = element_sum - digit_sum

Finally, return:
abs(a)

which is the required absolute difference.

📘 Example
Input:
nums = [1, 15, 6, 3]

Processing:
Add 1 → subtract 1
Add 15 → subtract 1 and 5
Add 6 → subtract 6
Add 3 → subtract 3
Element sum = 25
Digit sum = 16
Difference = |25 - 16| = 9

Output:
9

⏱️ TIME COMPLEXITY: O(n · k)
Where:
n = number of elements
k = digits per element
Still extremely fast.

🧠 SPACE COMPLEXITY: O(1)
Uses only one variable (a)."""