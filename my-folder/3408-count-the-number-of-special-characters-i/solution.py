class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for i in word:
            if(i.islower()):
                lower.add(i)
            else:
                upper.add(i.lower())
        return len(lower & upper)
