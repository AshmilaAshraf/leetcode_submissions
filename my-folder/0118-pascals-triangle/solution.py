class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1]]
        if(numRows == 1):
            return nums
        nums.append([1,1])
        if(numRows==2):
            return nums
        for i in range(2,numRows):
            k = [1,1]
            s = nums[i-1]
            for j in range(i-1):
                k.insert(1,(s[j]+s[j+1]))
            nums.append(k)
        return nums


