"""🧩 Problem: 2798. Number of Employees Who Met the Target

You are given:
A list hours where hours[i] is the number of hours the i-th employee worked.
An integer target.

Return the number of employees who worked at least target hours.
"""

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count

"""🧠 EXPLANATION

We simply check each employee's working hours:

If an employee worked greater than or equal to target, they qualify.

Increment count each time the condition is met.

Return the total count.

Very straightforward linear scan.

📘 Example

Input:
hours = [0, 1, 2, 3, 4]
target = 2

Check each value:
0 → no
1 → no
2 → yes
3 → yes
4 → yes
Total employees meeting target = 3

Output:
3

⏱️ TIME COMPLEXITY: O(n)
We iterate through the list once.

🧠 SPACE COMPLEXITY: O(1)
Uses only a counter, constant space.
"""