class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_chars = ""
            for c in word:
                next_c = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                next_chars += next_c
            word += next_chars
        return word[k - 1]
