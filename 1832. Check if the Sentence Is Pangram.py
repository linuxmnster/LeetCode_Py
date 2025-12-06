"""
🧩 Problem: 1832. Check if the Sentence Is Pangram
A pangram is a sentence that contains every letter of the English alphabet at least once.
Given a string sentence containing only lowercase English letters, return:
True if it is a pangram
False otherwise
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = set()
        for i in sentence:
            x.add(i)
            if len(x) == 26:
                return True
        return False
        # return len(set(sentence)) == 26

"""🧠 EXPLANATION
We use a set to track the unique letters we have seen.
Why a set?
A set automatically removes duplicates.

We only care about how many unique letters exist.
If the set size reaches 26, we know the sentence contains all letters → pangram.

Process
For each character i in the sentence:
Add it to the set
If the set size becomes 26, return True immediately (early stop → faster)
If loop finishes and size is < 26 → return False.

📘 Example
Input:
sentence = "thequickbrownfoxjumpsoverthelazydog"
Unique characters encountered → 26 letters
Output:
True


Another example:
Input:
sentence = "leetcode"
Unique characters = 7
Output:
False

⏱️ TIME COMPLEXITY: O(n)
We scan each character once.

🧠 SPACE COMPLEXITY: O(1)
Although we use a set, it can hold at most 26 characters, so space is constant."""