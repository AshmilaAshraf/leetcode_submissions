class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        
        num_list = []
        for i in range(0,n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j,k = i+1, n-1
            
            while(j<k):
                sums = nums[i] + nums[j]+ nums[k]
                if sums == 0:
                    num_list.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sums<0:
                    j+=1
                else:
                    k-=1
            
 
        return num_list

