class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))

        n = len(words)
        dp = [1] * n            
        prev = [-1] * n         

        for i in range(n):
            for j in range(i):
                if (
                    len(words[i]) == len(words[j]) and
                    hamming_distance(words[i], words[j]) == 1 and
                    groups[i] != groups[j]
                ):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # Find index of max dp value
        max_len = max(dp)
        index = dp.index(max_len)

        # Reconstruct the subsequence
        result = []
        while index != -1:
            result.append(words[index])
            index = prev[index]

        return result[::-1]
