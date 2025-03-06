class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = sum(grid, [])
        ans = [0,0]
        n = len(grid)
        s = sum(grid)
        k = sum(set(grid))
        ans[0] = s-k
        s = n*(n+1)//2
        ans[1] = abs(s-k)
        return(ans)





