class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        seen = {}
        nums1 = nums1 + nums2
        for i in range(len(nums1)):
            if nums1[i][0] in seen:
                seen[nums1[i][0]] += nums1[i][1]
            else:
                seen[nums1[i][0]] = nums1[i][1]
        return(sorted(map(list, seen.items())))

