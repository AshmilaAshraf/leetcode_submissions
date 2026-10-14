class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        # convert_list = ''
        # for i in range(n):
        #     if s[i].isalnum():
        #         convert_list+=s[i].lower()
        # j,k = 0, len(convert_list) -1
        # while(j<k):
        #     if convert_list[j] != convert_list[k]:
        #         return False
        #     j+=1
        #     k-=1
        # return True 
        left, right = 0, n-1
        while(left<right):
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                
                left+=1
                right-=1
        return True
