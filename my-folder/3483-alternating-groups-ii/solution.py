class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # c1 = colors.count(1)
        # c2 = colors.count(0)
        # cycleList = colors + colors[:k] 
        # n = len(colors)
        # if(n-k>1):
        #     cycleList = colors + colors[:k]
        # if(n-k <=1 and n%2 == 0):
        #     cycleList = colors + colors[:n//2]
        # if(n-k <=1 and n%2 != 0):
        #     cycleList = colors + colors[:n//2 +1]
        # # cycleList = colors + colors[:k] if n-k>1 else colors + colors[:k//2+1]

        # alter_list1 = [0, 1] * (k // 2) + [0] * (k % 2) 
        # alter_list2 = [1, 0] * (k // 2) + [1] * (k % 2)

        # cycle_str = "".join(map(str, cycleList))
        # alter_str1 = "".join(map(str, alter_list1))
        # alter_str2 = "".join(map(str, alter_list2))

        # count1 = cycle_str.count(alter_str1) if alter_str1 else 0
        # count2 = cycle_str.count(alter_str2) if alter_str2 else 0

        # return count1 + count2
        # # if(colors.count(1)-colors.count(0)>k//2):
        # #     return 0

        n = len(colors)
        count = 0
        valid_count = 0

        extended_colors = colors + colors[:k - 1]

        for i in range(k - 1):
            if extended_colors[i] != extended_colors[i + 1]:
                valid_count += 1

        for i in range(n):
            if valid_count == k - 1:
                count += 1

            if i + k < len(extended_colors):
                if extended_colors[i] != extended_colors[i + 1]:
                    valid_count -= 1
                if extended_colors[i + k - 1] != extended_colors[i + k]:
                    valid_count += 1

        return count
        # cycleList = colors + colors[:k-1]
        # c = 0
        # i=0
        # alter_list1 = [0, 1] * (k // 2) + [0] * (k % 2) 
        # alter_list2 = [1, 0] * (k // 2) + [1] * (k % 2)
        # # # alter_list1 = [(i) % 2 for i in range(k)]
        # # # alter_list2 = alter_list1[1:] + [alter_list1[0]]
        # while(i<len(colors)):
        #     subList = cycleList[i:i+k]
        #     if(subList == alter_list1 or subList == alter_list2):
        #         c = c+1
        #         i=i+1
        #         continue
        #     Flag = True
        #     for j in range(k):
        #         if(j+1<k and subList[j] == subList[j+1]):
        #             Flag = False
        #             i=i+j+1
        #             break
        #     if(Flag):
        #         c = c+1
        #         i = i + 1
                
        # return(c)
