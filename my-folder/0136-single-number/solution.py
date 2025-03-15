class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        s= sum(set(nums))
        return( (2*s) - sum(nums))
        
