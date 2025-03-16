class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i = 0
        # j = 0
        # while(i<(m+n)):
        #     if(nums2[j]<=nums1[i]):
        #         nums.insert(i,nums2[i])
        nums1[m:] = nums2
        # nums1 = sorted(nums1)
        for i in range(m+n):
            for j in range(m+n):
                if(j+1<m+n):
                    if(nums1[j]>nums1[j+1]):
                        temp = nums1[j]
                        nums1[j] = nums1[j+1]
                        nums1[j+1] = temp
        
