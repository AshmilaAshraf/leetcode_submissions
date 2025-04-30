class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k = count = 0
        for numb in nums:
            count = len(str(numb))
            if count % 2 == 0: k, count = k + 1, 0
            num_list = 0
        return k

