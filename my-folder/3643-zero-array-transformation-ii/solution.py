class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(x == 0 for x in nums):
            return 0
        
        n = len(nums)
        
        def can_make_zero_array(k):
            max_reduction = [0] * n
            
            for i in range(k):
                l, r, val = queries[i]
                max_reduction[l] += val
                if r + 1 < n:
                    max_reduction[r + 1] -= val
            
            curr_reduction = 0
            for i in range(n):
                curr_reduction += max_reduction[i]
                if curr_reduction < nums[i]:
                    return False
            
            return True
        
        left, right = 0, len(queries)
        while left < right:
            mid = (left + right) // 2
            if can_make_zero_array(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= len(queries) and can_make_zero_array(left) else -1
