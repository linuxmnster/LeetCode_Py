"""
🧩 Problem: 2114. Maximum Number of Words Found in Sentences

You are given an array of strings sentences.
Each string represents a sentence composed of words separated by single spaces.

Return the maximum number of words found in any single sentence.
"""

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        m = 0
        for i in sentences:
            if len(i.split()) > m:
                m = len(i.split())
        return m
        # return max(len(sentences[i]) for i in range(len(sentences)))
        # This can also be done by counting spaces.

"""🧠 EXPLANATION
How the logic works:
Each sentence is made up of words separated by spaces.
i.split() splits the sentence into a list of words.
len(i.split()) gives how many words are in that sentence.
You keep updating m to the largest number of words found so far.
Why split() works well?
split() automatically handles splitting by spaces and returns only the words — no empty strings.

📘 Example
Input:
sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
]

Word counts:
Sentence 1 → 5 words
Sentence 2 → 4 words
Sentence 3 → 6 words
Output:
6

⏱️ TIME COMPLEXITY: O(n * k)
Where:
n = number of sentences
k = average number of words per sentence (cost of split)
Still very fast for constraints.

🧠 SPACE COMPLEXITY: O(k)
split() temporarily stores words of one sentence → depends on size of one sentence, not all."""