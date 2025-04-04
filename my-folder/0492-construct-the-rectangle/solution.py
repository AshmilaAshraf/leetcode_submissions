class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = 1
        while W * W <= area:
            W += 1
        W -= 1 

        while area % W != 0:
            W -= 1

        L = area // W
        return [L, W]
