"""
🧩 Problem: 771. Jewels and Stones
You’re given two strings:
jewels: characters that represent types of jewels
stones: characters you have as stones
Return how many stones are also jewels.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        k = 0
        for i in stones:
            if i in jewels:
                k += 1
        return k

"""EXPLANATION"""
"""
Convert jewels string into a set for faster lookup (O(1) time per check).
Go through each character i in stones.
If i is found in the jewels set, increment k.
Finally, return k, which is the count of jewel stones you have.

🧠 Example:
Input: jewels = "aA", stones = "aAAbbbb"

a → jewel ✅

A → jewel ✅

A → jewel ✅

b → not jewel ❌ (4 times)

Total jewels = 3
"""