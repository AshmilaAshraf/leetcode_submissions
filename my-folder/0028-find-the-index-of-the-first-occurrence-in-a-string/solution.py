class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j,k = len(haystack), len(needle)
        if(needle not in haystack):
            return -1
        
        for i in range(0,j-k+1):
            if( haystack[i: i+k] == needle):
                return i
            
            
