class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(k == 0):
            return n

        sortedArray = sorted(nums)
        count = 0
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sortedArray[j + 1] == sortedArray[i]:
                j += 1
            
            if n - (j + 1) >= k:
                count += (j - i + 1)  
            i = j + 1
        return count
