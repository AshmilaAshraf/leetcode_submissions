class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        def findMid(l,r):
            return((l + r) // 2)

        mid = findMid(left,right)

        while(left<=right):
            if(nums[mid] == target):
                return mid
            if(nums[mid] < target):
                left = mid + 1
            if(nums[mid] > target):
                right = mid -1
            mid = findMid(left,right)
        else:
            return -1

