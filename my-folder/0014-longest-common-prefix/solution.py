class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = ''
        for i in range(len(min(strs))):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return stack
            stack += strs[0][i]
            
        return stack
        
