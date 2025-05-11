class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if(n<3):
            return False
        i=0
        while(i<n):
            if(arr[i] & 1):
                if(i+2<n):
                    if(arr[i+2] & 1):
                        if(arr[i+1] & 1):
                            return True
                        else:
                            i=i+2
                            continue
                    else:
                        i = i+3
                        continue
                else:
                    return False
            else:
                i = i+1
        return False


