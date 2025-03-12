class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        if(0 in nums):
            z_count = nums.count(0)
            # z_index = nums.index(0)
            neg = nums.index(0)
            pos = n- (z_count+neg)
            return(max(pos,neg))

        left  = 0
        right = n-1
        mid = (n-1)//2
        pos=0
        neg=0
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > 0:
                pos = n - mid
                right = mid - 1  
            else:
                neg = mid + 1
                left = mid + 1
        return(max(pos,neg))
        # while(mid>=0):
        #     if(nums[mid]>0):
        #         if(mid-1>=0):
        #             if(nums[mid-1]==0):
        #                 pos = n-mid
        #                 neg = n- (pos+nums.count(0))
        #                 # break
        #                 return(max(pos,neg))
        #             if(nums[mid-1]<0):
        #                 pos = n-mid
        #                 neg = n-pos
        #                 # break
        #                 return(max(pos,neg))

        #         else:
        #             # pos = n
        #             # neg = 0
        #             # break
        #             return(n)
        #         right = mid
        #         mid = (left+right)//2
        #         continue
        #     # if(nums[mid]<0):
        #     else:
        #         if(mid+1<n):
        #             if(nums[mid+1]==0):
        #                 neg = n-mid
        #                 pos = n- (neg+nums.count(0))
        #                 # break
        #                 return(max(pos,neg))
        #             if(nums[mid+1]<0):
        #                 neg = n-mid
        #                 pos = n-neg
        #                 # break
        #                 return(max(pos,neg))
        #         else:
        #             # neg = n
        #             # pos = 0
        #             # break
        #             return(n)
        #         left = mid
        #     mid = (left+right)//2
        #         # continue

