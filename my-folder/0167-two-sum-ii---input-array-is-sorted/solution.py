class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex=0
        n = len(numbers)
        rightIndex = n-1
        result = [1,n]
        while(leftIndex != rightIndex):
            k = numbers[leftIndex] + numbers[rightIndex]
            if(k == target):
                result = [leftIndex+1, rightIndex+1]
                break
            if(k<target):
                leftIndex+=1
                continue
            if(k>target):
                rightIndex-=1
                continue
        return result
